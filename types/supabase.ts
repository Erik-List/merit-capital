export type Json =
  | string
  | number
  | boolean
  | null
  | { [key: string]: Json | undefined }
  | Json[]

export type Database = {
  // Allows to automatically instantiate createClient with right options
  // instead of createClient<Database, { PostgrestVersion: 'XX' }>(URL, KEY)
  __InternalSupabase: {
    PostgrestVersion: "14.5"
  }
  public: {
    Tables: {
      companies: {
        Row: {
          created_at: string
          entry_stage: string
          focus: string | null
          hq_city: string | null
          hq_country: string | null
          id: string
          investor_id: string
          name: string
          seed_to_a_graduation: boolean | null
          status: string
          updated_at: string
          valuation_asof: string | null
          valuation_range: string
          valuation_usd: number | null
        }
        Insert: {
          created_at?: string
          entry_stage: string
          focus?: string | null
          hq_city?: string | null
          hq_country?: string | null
          id?: string
          investor_id: string
          name: string
          seed_to_a_graduation?: boolean | null
          status: string
          updated_at?: string
          valuation_asof?: string | null
          valuation_range: string
          valuation_usd?: number | null
        }
        Update: {
          created_at?: string
          entry_stage?: string
          focus?: string | null
          hq_city?: string | null
          hq_country?: string | null
          id?: string
          investor_id?: string
          name?: string
          seed_to_a_graduation?: boolean | null
          status?: string
          updated_at?: string
          valuation_asof?: string | null
          valuation_range?: string
          valuation_usd?: number | null
        }
        Relationships: [
          {
            foreignKeyName: "companies_investor_id_fkey"
            columns: ["investor_id"]
            isOneToOne: false
            referencedRelation: "investors"
            referencedColumns: ["id"]
          },
        ]
      }
      investors: {
        Row: {
          affiliation: Json | null
          aum: Json | null
          company_focus_distribution: Json | null
          company_geo_distribution: Json | null
          company_stage_distribution: Json | null
          created_at: string
          founding_year: number | null
          funds: Json | null
          graduation_rate: Json | null
          history: string | null
          hq_location: string | null
          icon_url: string | null
          id: string
          individuals: Json | null
          investment_concept: string | null
          investment_geo: Json | null
          investment_range: Json | null
          investment_scope: Json | null
          investment_stage: Json | null
          investor_type: Database["public"]["Enums"]["InvestorType"]
          name: string
          notable_investments: Json | null
          slug: string
          track_record: Json | null
          updated_at: string
          website: string | null
        }
        Insert: {
          affiliation?: Json | null
          aum?: Json | null
          company_focus_distribution?: Json | null
          company_geo_distribution?: Json | null
          company_stage_distribution?: Json | null
          created_at?: string
          founding_year?: number | null
          funds?: Json | null
          graduation_rate?: Json | null
          history?: string | null
          hq_location?: string | null
          icon_url?: string | null
          id?: string
          individuals?: Json | null
          investment_concept?: string | null
          investment_geo?: Json | null
          investment_range?: Json | null
          investment_scope?: Json | null
          investment_stage?: Json | null
          investor_type?: Database["public"]["Enums"]["InvestorType"]
          name: string
          notable_investments?: Json | null
          slug: string
          track_record?: Json | null
          updated_at: string
          website?: string | null
        }
        Update: {
          affiliation?: Json | null
          aum?: Json | null
          company_focus_distribution?: Json | null
          company_geo_distribution?: Json | null
          company_stage_distribution?: Json | null
          created_at?: string
          founding_year?: number | null
          funds?: Json | null
          graduation_rate?: Json | null
          history?: string | null
          hq_location?: string | null
          icon_url?: string | null
          id?: string
          individuals?: Json | null
          investment_concept?: string | null
          investment_geo?: Json | null
          investment_range?: Json | null
          investment_scope?: Json | null
          investment_stage?: Json | null
          investor_type?: Database["public"]["Enums"]["InvestorType"]
          name?: string
          notable_investments?: Json | null
          slug?: string
          track_record?: Json | null
          updated_at?: string
          website?: string | null
        }
        Relationships: []
      }
    }
    Views: {
      [_ in never]: never
    }
    Functions: {
      recompute_investor_metrics: {
        Args: { target_investor_id: string }
        Returns: undefined
      }
    }
    Enums: {
      InvestorType: "Institutional" | "Individual"
    }
    CompositeTypes: {
      [_ in never]: never
    }
  }
}

type DatabaseWithoutInternals = Omit<Database, "__InternalSupabase">

type DefaultSchema = DatabaseWithoutInternals[Extract<keyof Database, "public">]

export type Tables<
  DefaultSchemaTableNameOrOptions extends
    | keyof (DefaultSchema["Tables"] & DefaultSchema["Views"])
    | { schema: keyof DatabaseWithoutInternals },
  TableName extends DefaultSchemaTableNameOrOptions extends {
    schema: keyof DatabaseWithoutInternals
  }
    ? keyof (DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"] &
        DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Views"])
    : never = never,
> = DefaultSchemaTableNameOrOptions extends {
  schema: keyof DatabaseWithoutInternals
}
  ? (DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"] &
      DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Views"])[TableName] extends {
      Row: infer R
    }
    ? R
    : never
  : DefaultSchemaTableNameOrOptions extends keyof (DefaultSchema["Tables"] &
        DefaultSchema["Views"])
    ? (DefaultSchema["Tables"] &
        DefaultSchema["Views"])[DefaultSchemaTableNameOrOptions] extends {
        Row: infer R
      }
      ? R
      : never
    : never

export type TablesInsert<
  DefaultSchemaTableNameOrOptions extends
    | keyof DefaultSchema["Tables"]
    | { schema: keyof DatabaseWithoutInternals },
  TableName extends DefaultSchemaTableNameOrOptions extends {
    schema: keyof DatabaseWithoutInternals
  }
    ? keyof DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"]
    : never = never,
> = DefaultSchemaTableNameOrOptions extends {
  schema: keyof DatabaseWithoutInternals
}
  ? DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"][TableName] extends {
      Insert: infer I
    }
    ? I
    : never
  : DefaultSchemaTableNameOrOptions extends keyof DefaultSchema["Tables"]
    ? DefaultSchema["Tables"][DefaultSchemaTableNameOrOptions] extends {
        Insert: infer I
      }
      ? I
      : never
    : never

export type TablesUpdate<
  DefaultSchemaTableNameOrOptions extends
    | keyof DefaultSchema["Tables"]
    | { schema: keyof DatabaseWithoutInternals },
  TableName extends DefaultSchemaTableNameOrOptions extends {
    schema: keyof DatabaseWithoutInternals
  }
    ? keyof DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"]
    : never = never,
> = DefaultSchemaTableNameOrOptions extends {
  schema: keyof DatabaseWithoutInternals
}
  ? DatabaseWithoutInternals[DefaultSchemaTableNameOrOptions["schema"]]["Tables"][TableName] extends {
      Update: infer U
    }
    ? U
    : never
  : DefaultSchemaTableNameOrOptions extends keyof DefaultSchema["Tables"]
    ? DefaultSchema["Tables"][DefaultSchemaTableNameOrOptions] extends {
        Update: infer U
      }
      ? U
      : never
    : never

export type Enums<
  DefaultSchemaEnumNameOrOptions extends
    | keyof DefaultSchema["Enums"]
    | { schema: keyof DatabaseWithoutInternals },
  EnumName extends DefaultSchemaEnumNameOrOptions extends {
    schema: keyof DatabaseWithoutInternals
  }
    ? keyof DatabaseWithoutInternals[DefaultSchemaEnumNameOrOptions["schema"]]["Enums"]
    : never = never,
> = DefaultSchemaEnumNameOrOptions extends {
  schema: keyof DatabaseWithoutInternals
}
  ? DatabaseWithoutInternals[DefaultSchemaEnumNameOrOptions["schema"]]["Enums"][EnumName]
  : DefaultSchemaEnumNameOrOptions extends keyof DefaultSchema["Enums"]
    ? DefaultSchema["Enums"][DefaultSchemaEnumNameOrOptions]
    : never

export type CompositeTypes<
  PublicCompositeTypeNameOrOptions extends
    | keyof DefaultSchema["CompositeTypes"]
    | { schema: keyof DatabaseWithoutInternals },
  CompositeTypeName extends PublicCompositeTypeNameOrOptions extends {
    schema: keyof DatabaseWithoutInternals
  }
    ? keyof DatabaseWithoutInternals[PublicCompositeTypeNameOrOptions["schema"]]["CompositeTypes"]
    : never = never,
> = PublicCompositeTypeNameOrOptions extends {
  schema: keyof DatabaseWithoutInternals
}
  ? DatabaseWithoutInternals[PublicCompositeTypeNameOrOptions["schema"]]["CompositeTypes"][CompositeTypeName]
  : PublicCompositeTypeNameOrOptions extends keyof DefaultSchema["CompositeTypes"]
    ? DefaultSchema["CompositeTypes"][PublicCompositeTypeNameOrOptions]
    : never

export const Constants = {
  public: {
    Enums: {
      InvestorType: ["Institutional", "Individual"],
    },
  },
} as const
