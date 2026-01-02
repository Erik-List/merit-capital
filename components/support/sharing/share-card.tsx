"use client";

import { useState, useEffect } from "react";
import { Copy, Check } from "lucide-react";
import { LinkedinLogoIcon, XLogoIcon } from "@phosphor-icons/react";
import { Button } from "@/components/ui/button";
import { useToast } from "@/hooks/use-toast";
import { WhatsAppIcon } from "@/components/icons/whatsapp-icon";
import { createClient } from "@/utils/supabase/client";

// Helper function to generate share URL with optional share code
function getShareUrl(shareCode?: string): string {
  const baseUrl = "https://meritcapit.al";
  if (shareCode) {
    return `${baseUrl}?shared-by=${encodeURIComponent(shareCode)}`;
  }
  return baseUrl;
}

// Deep link helper functions
function getWhatsAppLink(message: string): string {
  return `https://wa.me/?text=${encodeURIComponent(message)}`;
}

function getLinkedInPostLink(url: string): string {
  return `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(url)}`;
}

function getTwitterPostLink(text: string): string {
  return `https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}`;
}

interface ShareCardProps {
  shareLink: string;
  isFormComplete: boolean;
  firstName: string;
  lastName: string;
  shareCode?: string; // Keep for backward compatibility but use shareLink instead
  isActivated?: boolean; // Whether the sharing link is activated
}

export function ShareCard({ 
  shareLink, 
  isFormComplete, 
  firstName, 
  lastName,
  shareCode,
  isActivated = false
}: ShareCardProps) {
  const { toast } = useToast();
  const [copied, setCopied] = useState(false);
  const [linkExists, setLinkExists] = useState(false);
  
  // Use dynamic shareLink if provided, otherwise fall back to shareCode
  const meritCapitalUrl = shareLink || getShareUrl(shareCode);
  const shareMessage = `Take a look at Merit Capital - ${meritCapitalUrl}`;

  // Check if sharing link exists in database based on firstName and lastName
  // If isActivated is true, skip database check and set linkExists to true
  useEffect(() => {
    if (isActivated) {
      setLinkExists(true);
      return;
    }

    const checkSharingLinkExists = async () => {
      if (!firstName.trim() || !lastName.trim()) {
        setLinkExists(false);
        return;
      }

      try {
        const supabase = createClient();
        const { data, error } = await supabase
          .from('Supporters')
          .select('sharing_link_active')
          .eq('first_name', firstName.trim())
          .eq('last_name', lastName.trim())
          .eq('sharing_link_active', true)
          .limit(1);

        if (error) {
          console.error('Error checking sharing link:', error);
          setLinkExists(false);
        } else {
          setLinkExists(data && data.length > 0);
        }
      } catch (error) {
        console.error('Error checking sharing link:', error);
        setLinkExists(false);
      }
    };

    checkSharingLinkExists();
  }, [firstName, lastName, isActivated]);

  const handleCopyLink = async () => {
    if (!linkExists) {
      toast({
        title: "Sharing link not found",
        description: "Get your sharing link by filling out the form and declaring support for Merit Capital.",
      });
      return;
    }

    try {
      await navigator.clipboard.writeText(meritCapitalUrl);
      setCopied(true);
      setTimeout(() => {
        setCopied(false);
      }, 2000);
    } catch (error) {
      toast({
        title: "Failed to copy",
        description: "Please try again.",
        variant: "destructive",
      });
    }
  };

  const handleShare = (platform: "whatsapp" | "linkedin" | "twitter") => {
    if (!linkExists) {
      toast({
        title: "Sharing link not found",
        description: "Get your sharing link by filling out the form and declaring support for Merit Capital.",
      });
      return;
    }

    let url: string;
    
    switch (platform) {
      case "whatsapp":
        url = getWhatsAppLink(shareMessage);
        break;
      case "linkedin":
        url = getLinkedInPostLink(meritCapitalUrl);
        break;
      case "twitter":
        url = getTwitterPostLink(shareMessage);
        break;
    }
    
    window.open(url, "_blank", "noopener,noreferrer");
  };

  return (
    <div className="space-y-4">
      <div className="space-y-0">
        <h3 className="text-xl font-semibold">
          Share Merit Capital with your network.
        </h3>
        <p className="text-sm text-muted-foreground">
          Get your sharing link to spread the word of Merit Capital.
        </p>
      </div>
      
      <div className="space-y-2">
        <div className="flex items-center gap-2">
          <a
            href={meritCapitalUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="text-sm text-primary underline underline-offset-4"
          >
            {meritCapitalUrl}
          </a>
          <button
            onClick={handleCopyLink}
            className="inline-flex items-center gap-1.5 justify-center hover:opacity-70 transition-opacity"
            aria-label="Copy link"
          >
            {copied ? (
              <Check className="h-4 w-4 text-muted-foreground" />
            ) : (
              <Copy className="h-4 w-4 text-muted-foreground" />
            )}
            {isActivated ? (
              <span className="text-xs text-muted-foreground">activated</span>
            ) : (firstName.trim() || lastName.trim()) ? (
              <span className="text-xs text-muted-foreground">not activated</span>
            ) : null}
          </button>
        </div>

        <div className="flex items-center gap-2">
          <span className="text-base font-medium">Share on</span>
          <Button
            variant="outline"
            size="icon"
            onClick={() => handleShare("whatsapp")}
            className="h-10 w-10"
            aria-label="Share on WhatsApp"
          >
            <WhatsAppIcon className="h-5 w-5" />
          </Button>
          
          <Button
            variant="outline"
            size="icon"
            onClick={() => handleShare("linkedin")}
            className="h-10 w-10"
            aria-label="Share on LinkedIn"
          >
            <LinkedinLogoIcon className="h-6 w-6" weight="regular" />
          </Button>
          
          <Button
            variant="outline"
            size="icon"
            onClick={() => handleShare("twitter")}
            className="h-10 w-10"
            aria-label="Share on X"
          >
            <XLogoIcon className="h-6 w-6" weight="regular" />
          </Button>
        </div>
      </div>
    </div>
  );
}














