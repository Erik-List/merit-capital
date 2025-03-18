export type Json =
  | string
  | number
  | boolean
  | null
  | { [key: string]: Json | undefined }
  | Json[]

export type Database = {
  public: {
    Tables: {
      Investor: {
        Row: {
          aum: string | null
          created_at: string
          funds_info: Json | null
          history: string | null
          hq_location: string | null
          id: string
          investment_concept: string | null
          investment_focus: Json | null
          investment_geo: Json | null
          investment_range: Json | null
          investment_scope: Database["public"]["Enums"]["InvestmentScope"] | null
          investment_stage: string | null
          investment_style: string | null
          investor_type: string | null
          logo_url: string | null
          name: string
          notable_investments: Json | null
          other_locations: Json | null
          partners: Json | null
          slug: string
          status: Database["public"]["Enums"]["ApprovalStatus"]
          updated_at: string
        }
        Insert: {
          aum?: string | null
          created_at?: string
          funds_info?: Json | null
          history?: string | null
          hq_location?: string | null
          id: string
          investment_concept?: string | null
          investment_focus?: Json | null
          investment_geo?: Json | null
          investment_range?: Json | null
          investment_scope?: Database["public"]["Enums"]["InvestmentScope"] | null
          investment_stage?: string | null
          investment_style?: string | null
          investor_type?: string | null
          logo_url?: string | null
          name: string
          notable_investments?: Json | null
          other_locations?: Json | null
          partners?: Json | null
          slug: string
          status?: Database["public"]["Enums"]["ApprovalStatus"]
          updated_at: string
        }
        Update: {
          aum?: string | null
          created_at?: string
          funds_info?: Json | null
          history?: string | null
          hq_location?: string | null
          id?: string
          investment_concept?: string | null
          investment_focus?: Json | null
          investment_geo?: Json | null
          investment_range?: Json | null
          investment_scope?: Database["public"]["Enums"]["InvestmentScope"] | null
          investment_stage?: string | null
          investment_style?: string | null
          investor_type?: string | null
          logo_url?: string | null
          name?: string
          notable_investments?: Json | null
          other_locations?: Json | null
          partners?: Json | null
          slug?: string
          status?: Database["public"]["Enums"]["ApprovalStatus"]
          updated_at?: string
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
      [_ in never]: never
    }
    Functions: {
      [_ in never]: never
    }
    Enums: {
      ApprovalStatus: "PENDING_APPROVAL" | "APPROVED" | "REJECTED"
      InvestmentScope: "GENERALIST" | "SPECIALIST"
      RatingType: "NEW" | "UPDATE" | "DELETION"
    }
    CompositeTypes: {
      [_ in never]: never
    }
  }
}

type PublicSchema = Database[Extract<keyof Database, "public">]

export type Tables<
  PublicTableNameOrOptions extends
    | keyof (PublicSchema["Tables"] & PublicSchema["Views"])
    | { schema: keyof Database },
  TableName extends PublicTableNameOrOptions extends { schema: keyof Database }
    ? keyof (Database[PublicTableNameOrOptions["schema"]]["Tables"] &
        Database[PublicTableNameOrOptions["schema"]]["Views"])
    : never = never,
> = PublicTableNameOrOptions extends { schema: keyof Database }
  ? (Database[PublicTableNameOrOptions["schema"]]["Tables"] &
      Database[PublicTableNameOrOptions["schema"]]["Views"])[TableName] extends {
      Row: infer R
    }
    ? R
    : never
  : PublicTableNameOrOptions extends keyof (PublicSchema["Tables"] &
        PublicSchema["Views"])
    ? (PublicSchema["Tables"] &
        PublicSchema["Views"])[PublicTableNameOrOptions] extends {
        Row: infer R
      }
      ? R
      : never
    : never

export type TablesInsert<
  PublicTableNameOrOptions extends
    | keyof PublicSchema["Tables"]
    | { schema: keyof Database },
  TableName extends PublicTableNameOrOptions extends { schema: keyof Database }
    ? keyof Database[PublicTableNameOrOptions["schema"]]["Tables"]
    : never = never,
> = PublicTableNameOrOptions extends { schema: keyof Database }
  ? Database[PublicTableNameOrOptions["schema"]]["Tables"][TableName] extends {
      Insert: infer I
    }
    ? I
    : never
  : PublicTableNameOrOptions extends keyof PublicSchema["Tables"]
    ? PublicSchema["Tables"][PublicTableNameOrOptions] extends {
        Insert: infer I
      }
      ? I
      : never
    : never

export type TablesUpdate<
  PublicTableNameOrOptions extends
    | keyof PublicSchema["Tables"]
    | { schema: keyof Database },
  TableName extends PublicTableNameOrOptions extends { schema: keyof Database }
    ? keyof Database[PublicTableNameOrOptions["schema"]]["Tables"]
    : never = never,
> = PublicTableNameOrOptions extends { schema: keyof Database }
  ? Database[PublicTableNameOrOptions["schema"]]["Tables"][TableName] extends {
      Update: infer U
    }
    ? U
    : never
  : PublicTableNameOrOptions extends keyof PublicSchema["Tables"]
    ? PublicSchema["Tables"][PublicTableNameOrOptions] extends {
        Update: infer U
      }
      ? U
      : never
    : never

export type Enums<
  PublicEnumNameOrOptions extends
    | keyof PublicSchema["Enums"]
    | { schema: keyof Database },
  EnumName extends PublicEnumNameOrOptions extends { schema: keyof Database }
    ? keyof Database[PublicEnumNameOrOptions["schema"]]["Enums"]
    : never = never,
> = PublicEnumNameOrOptions extends { schema: keyof Database }
  ? Database[PublicEnumNameOrOptions["schema"]]["Enums"][EnumName]
  : PublicEnumNameOrOptions extends keyof PublicSchema["Enums"]
    ? PublicSchema["Enums"][PublicEnumNameOrOptions]
    : never

export type CompositeTypes<
  PublicCompositeTypeNameOrOptions extends
    | keyof PublicSchema["CompositeTypes"]
    | { schema: keyof Database },
  CompositeTypeName extends PublicCompositeTypeNameOrOptions extends {
    schema: keyof Database
  }
    ? keyof Database[PublicCompositeTypeNameOrOptions["schema"]]["CompositeTypes"]
    : never = never,
> = PublicCompositeTypeNameOrOptions extends { schema: keyof Database }
  ? Database[PublicCompositeTypeNameOrOptions["schema"]]["CompositeTypes"][CompositeTypeName]
  : PublicCompositeTypeNameOrOptions extends keyof PublicSchema["CompositeTypes"]
    ? PublicSchema["CompositeTypes"][PublicCompositeTypeNameOrOptions]
    : never
