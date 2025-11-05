import { readCache, writeCache, cacheExists } from "./cache";
import { loadPrompt, getPromptHash } from "./prompts";
import OpenAI from "openai";

interface ModelResponse {
  data: any;
  promptHash: string;
}

// Configuration constants
const MAX_RETRIES = 3;
const RETRY_DELAY_MS = 1000;
const MODEL = "gpt-5";
const API_KEY = process.env.OPENAI_API_KEY;

if (!API_KEY) {
  throw new Error("OPENAI_API_KEY environment variable must be set");
}

const openai = new OpenAI({
  apiKey: API_KEY,
});

async function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function callOpenAI(
  prompt: string,
  investorName: string,
  jsonMode: boolean = true
): Promise<any> {
  // Build the system prompt with the loaded prompt template
  const systemPrompt = `You are a world class data aggregator. You are given an investor name and specific fields to aggregate. If you do your job well you will improve the world by making VC performance more transparent.\n\n${prompt}`;

  const requestBody: any = {
    model: MODEL,
    input: [
      {
        role: "developer",
        content: [
          {
            type: "input_text",
            text: systemPrompt,
          },
        ],
      },
      {
        role: "user",
        content: [
          {
            type: "input_text",
            text: `Investor: ${investorName}`,
          },
        ],
      },
    ],
    text: {
      format: {
        type: "text",
      },
      verbosity: "medium",
    },
    reasoning: {
      effort: "medium",
      summary: null,
    },
    tools: [
      {
        type: "web_search",
        user_location: {
          type: "approximate",
        },
        search_context_size: "medium",
      },
    ],
    store: true,
    include: [
      "reasoning.encrypted_content",
      "web_search_call.action.sources",
    ],
  };

  let lastError: Error | null = null;
  for (let attempt = 0; attempt < MAX_RETRIES; attempt++) {
    try {
      const response = await (openai as any).responses.create(requestBody);

      // Extract content from response
      let content: string | null = null;
      
      if (response.output?.[0]?.content) {
        const outputContent = response.output[0].content;
        if (Array.isArray(outputContent)) {
          content = outputContent
            .map((item: any) => item.text || item.content || "")
            .join("");
        } else if (typeof outputContent === "string") {
          content = outputContent;
        }
      }

      if (!content) {
        throw new Error("No content in OpenAI response");
      }

      // Parse JSON from response
      try {
        return JSON.parse(content);
      } catch (parseError) {
        // Sometimes JSON is wrapped in markdown code blocks
        const jsonMatch = content.match(/```(?:json)?\s*(\{[\s\S]*\})\s*```/);
        if (jsonMatch) {
          return JSON.parse(jsonMatch[1]);
        }
        throw new Error(`Failed to parse JSON from response: ${content.substring(0, 200)}`);
      }
    } catch (error) {
      lastError = error instanceof Error ? error : new Error(String(error));
      if (attempt < MAX_RETRIES - 1) {
        const delay = RETRY_DELAY_MS * (attempt + 1);
        console.warn(`Attempt ${attempt + 1} failed, retrying in ${delay}ms...`, lastError.message);
        await sleep(delay);
      }
    }
  }

  throw lastError || new Error("Failed to call OpenAI API");
}

export async function callModel(
  promptName: string,
  investorName: string,
  investorType: "Institutional" | "Individual"
): Promise<any> {
  // Load prompt with investor type
  const promptTemplate = loadPrompt(promptName, investorType);
  const promptHash = getPromptHash(promptName, investorType);

  // Check cache with prompt hash for invalidation
  // If the prompt file changes, the hash changes, so old cached responses are invalidated
  // Include investor type in cache key to prevent cross-contamination
  const cacheKey = `${promptName}-${investorType}-${investorName.toLowerCase().replace(/\s+/g, "-")}`;
  const cached = readCache<ModelResponse>(promptName, cacheKey);
  
  if (cached && cached.promptHash === promptHash) {
    console.log(`Using cached response for ${investorName} (${promptName})`);
    return cached.data;
  }

  let result: any;

  try {
    result = await callOpenAI(promptTemplate, investorName);

    // Cache the result with prompt hash
    writeCache<ModelResponse>(promptName, cacheKey, {
      data: result,
      promptHash,
    });

    return result;
  } catch (error) {
    console.error(`Model call failed for ${investorName} (${promptName}):`, error);
    throw error;
  }
}
