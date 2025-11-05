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
    PostgrestVersion: "12.2.3 (519615d)"
  }
  public: {
    Tables: {
      IndividualInvestor: {
        Row: {
          affiliation: Json | null
          investor_id: string
        }
        Insert: {
          affiliation?: Json | null
          investor_id: string
        }
        Update: {
          affiliation?: Json | null
          investor_id?: string
        }
        Relationships: [
          {
            foreignKeyName: "IndividualInvestor_investor_id_fkey"
            columns: ["investor_id"]
            isOneToOne: true
            referencedRelation: "Investor"
            referencedColumns: ["id"]
          },
          {
            foreignKeyName: "IndividualInvestor_investor_id_fkey"
            columns: ["investor_id"]
            isOneToOne: true
            referencedRelation: "InvestorView"
            referencedColumns: ["id"]
          },
        ]
      }
      InstitutionalInvestor: {
        Row: {
          aum: Json | null
          founding_year: number | null
          funds: Json | null
          individual: Json | null
          investor_id: string
        }
        Insert: {
          aum?: Json | null
          founding_year?: number | null
          funds?: Json | null
          individual?: Json | null
          investor_id: string
        }
        Update: {
          aum?: Json | null
          founding_year?: number | null
          funds?: Json | null
          individual?: Json | null
          investor_id?: string
        }
        Relationships: [
          {
            foreignKeyName: "InstitutionalInvestor_investor_id_fkey"
            columns: ["investor_id"]
            isOneToOne: true
            referencedRelation: "Investor"
            referencedColumns: ["id"]
          },
          {
            foreignKeyName: "InstitutionalInvestor_investor_id_fkey"
            columns: ["investor_id"]
            isOneToOne: true
            referencedRelation: "InvestorView"
            referencedColumns: ["id"]
          },
        ]
      }
      Investor: {
        Row: {
          created_at: string
          graduation_rate: Json | null
          history: string | null
          hq_location: string | null
          icon_url: string | null
          id: string
          investment_concept: string | null
          investment_focus: Json | null
          investment_geo: Json | null
          investment_range: Json | null
          investment_scope: Json | null
          investment_stage: Json | null
          investor_type: Database["public"]["Enums"]["InvestorType"]
          name: string
          notable_investments: Json | null
          other_locations: Json | null
          slug: string
          status: Database["public"]["Enums"]["ApprovalStatus"]
          track_record: Json | null
          updated_at: string
          website: string | null
        }
        Insert: {
          created_at?: string
          graduation_rate?: Json | null
          history?: string | null
          hq_location?: string | null
          icon_url?: string | null
          id: string
          investment_concept?: string | null
          investment_focus?: Json | null
          investment_geo?: Json | null
          investment_range?: Json | null
          investment_scope?: Json | null
          investment_stage?: Json | null
          investor_type?: Database["public"]["Enums"]["InvestorType"]
          name: string
          notable_investments?: Json | null
          other_locations?: Json | null
          slug: string
          status?: Database["public"]["Enums"]["ApprovalStatus"]
          track_record?: Json | null
          updated_at: string
          website?: string | null
        }
        Update: {
          created_at?: string
          graduation_rate?: Json | null
          history?: string | null
          hq_location?: string | null
          icon_url?: string | null
          id?: string
          investment_concept?: string | null
          investment_focus?: Json | null
          investment_geo?: Json | null
          investment_range?: Json | null
          investment_scope?: Json | null
          investment_stage?: Json | null
          investor_type?: Database["public"]["Enums"]["InvestorType"]
          name?: string
          notable_investments?: Json | null
          other_locations?: Json | null
          slug?: string
          status?: Database["public"]["Enums"]["ApprovalStatus"]
          track_record?: Json | null
          updated_at?: string
          website?: string | null
        }
        Relationships: []
      }
      Rating: {
        Row: {
          comments: Json
          created_at: string
          id: string
          investor_id: string
          log_message: string | null
          position_of_founder: string | null
          rating_type: Database["public"]["Enums"]["RatingType"] | null
          score: Json
          stage_of_company: string | null
          status: Database["public"]["Enums"]["ApprovalStatus"]
          updated_at: string
          user_id: string
        }
        Insert: {
          comments: Json
          created_at?: string
          id: string
          investor_id: string
          log_message?: string | null
          position_of_founder?: string | null
          rating_type?: Database["public"]["Enums"]["RatingType"] | null
          score: Json
          stage_of_company?: string | null
          status?: Database["public"]["Enums"]["ApprovalStatus"]
          updated_at: string
          user_id: string
        }
        Update: {
          comments?: Json
          created_at?: string
          id?: string
          investor_id?: string
          log_message?: string | null
          position_of_founder?: string | null
          rating_type?: Database["public"]["Enums"]["RatingType"] | null
          score?: Json
          stage_of_company?: string | null
          status?: Database["public"]["Enums"]["ApprovalStatus"]
          updated_at?: string
          user_id?: string
        }
        Relationships: [
          {
            foreignKeyName: "Rating_investor_id_fkey"
            columns: ["investor_id"]
            isOneToOne: false
            referencedRelation: "Investor"
            referencedColumns: ["id"]
          },
          {
            foreignKeyName: "Rating_investor_id_fkey"
            columns: ["investor_id"]
            isOneToOne: false
            referencedRelation: "InvestorView"
            referencedColumns: ["id"]
          },
          {
            foreignKeyName: "Rating_user_id_fkey"
            columns: ["user_id"]
            isOneToOne: false
            referencedRelation: "User"
            referencedColumns: ["id"]
          },
        ]
      }
      User: {
        Row: {
          created_at: string
          id: string
          linkedin_url: string
          updated_at: string
        }
        Insert: {
          created_at?: string
          id: string
          linkedin_url: string
          updated_at: string
        }
        Update: {
          created_at?: string
          id?: string
          linkedin_url?: string
          updated_at?: string
        }
        Relationships: []
      }
    }
    Views: {
      InvestorView: {
        Row: {
          affiliation: Json | null
          aum: Json | null
          created_at: string | null
          founding_year: number | null
          funds: Json | null
          graduation_rate: Json | null
          history: string | null
          hq_location: string | null
          icon_url: string | null
          id: string | null
          individual: Json | null
          investment_concept: string | null
          investment_focus: Json | null
          investment_geo: Json | null
          investment_range: Json | null
          investment_scope: Json | null
          investment_stage: Json | null
          investor_type: Database["public"]["Enums"]["InvestorType"] | null
          name: string | null
          notable_investments: Json | null
          other_locations: Json | null
          slug: string | null
          status: Database["public"]["Enums"]["ApprovalStatus"] | null
          track_record: Json | null
          updated_at: string | null
          website: string | null
        }
        Relationships: []
      }
    }
    Functions: {
      [_ in never]: never
    }
    Enums: {
      ApprovalStatus: "PENDING_APPROVAL" | "APPROVED" | "REJECTED"
      InvestorType: "Institutional" | "Individual"
      RatingType: "NEW" | "UPDATE" | "DELETION"
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
      ApprovalStatus: ["PENDING_APPROVAL", "APPROVED", "REJECTED"],
      InvestorType: ["Institutional", "Individual"],
      RatingType: ["NEW", "UPDATE", "DELETION"],
    },
  },
} as const
