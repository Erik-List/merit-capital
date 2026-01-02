"use client";

import { useEffect } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
} from "@/components/ui/form";
import { createClient } from "@/utils/supabase/client";
import { trackFormSubmission } from "@/lib/tracking";
import { getSharingToken } from "@/lib/sharing-token-storage";
import { useToast } from "@/hooks/use-toast";
import { ToastAction } from "@/components/ui/toast";

const formSchema = z.object({
  firstName: z.string().min(1, "First name is required"),
  lastName: z.string().min(1, "Last name is required"),
  company: z.string().min(1, "Company is required"),
  position: z.string().min(1, "Position is required"),
  email: z.string().email("Invalid email address"),
});

type FormValues = z.infer<typeof formSchema>;

interface SupportFormProps {
  onFormChange?: (values: {
    firstName: string;
    lastName: string;
    isFormComplete: boolean;
  }) => void;
}

export function SupportForm({ onFormChange }: SupportFormProps) {
  const form = useForm<FormValues>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      firstName: "",
      lastName: "",
      company: "",
      position: "",
      email: "",
    },
    mode: "onChange", // Enable real-time validation
  });

  const formValues = form.watch();
  const isFormValid = form.formState.isValid;
  const areAllFieldsFilled = 
    formValues.firstName.trim() !== "" &&
    formValues.lastName.trim() !== "" &&
    formValues.company.trim() !== "" &&
    formValues.position.trim() !== "" &&
    formValues.email.trim() !== "";
  
  const isDisabled = !isFormValid || !areAllFieldsFilled;
  const isFormComplete = !isDisabled;

  // Notify parent of form changes
  useEffect(() => {
    if (onFormChange) {
      onFormChange({
        firstName: formValues.firstName || "",
        lastName: formValues.lastName || "",
        isFormComplete,
      });
    }
  }, [formValues.firstName, formValues.lastName, isFormComplete, onFormChange]);

  const { toast } = useToast();

  const handleResendEmail = async (email: string) => {
    try {
      const response = await fetch('/api/support/resend-confirmation-email', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email }),
      });

      if (!response.ok) {
        const data = await response.json();
        throw new Error(data.error || 'Failed to resend email');
      }

      toast({
        title: "Email sent!",
        description: "Please check your inbox to confirm your email address.",
      });
    } catch (error) {
      toast({
        title: "Error",
        description: error instanceof Error ? error.message : "Failed to resend email. Please try again.",
        variant: "destructive",
      });
    }
  };

  const onSubmit = async (values: FormValues) => {
    try {
      const supabase = createClient();
      
      // Get referrer token from URL or storage
      const sharedByToken = getSharingToken();
      
      // Insert supporter record (client-side database function)
      const { data: result, error: dbError } = await supabase.rpc('insert_supporter', {
        p_first_name: values.firstName,
        p_last_name: values.lastName,
        p_company: values.company,
        p_position: values.position,
        p_email: values.email,
        p_referred_by_token: sharedByToken || null,
      });
      
      if (dbError) {
        if (dbError.code === '23505' || dbError.message?.includes('already registered')) {
          toast({
            title: "Email already registered",
            description: "This email is already registered and confirmed.",
            action: (
              <ToastAction altText="Resend email" onClick={() => handleResendEmail(values.email)}>
                Resend
              </ToastAction>
            ),
          });
          return;
        }
        throw new Error(dbError.message || 'Failed to submit form');
      }
      
      // Send confirmation email (API route)
      const emailResponse = await fetch('/api/support/send-confirmation-email', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email: result.email,
          firstName: result.first_name,
          confirmationToken: result.confirmation_token,
        }),
      });
      
      if (!emailResponse.ok) {
        // Don't fail - supporter is already inserted
        console.error('Failed to send confirmation email');
      }
      
      // Track in PostHog (client-side)
      trackFormSubmission(sharedByToken);
      
      toast({
        title: "Email sent!",
        description: "Please check your inbox to confirm your email address.",
      });
    } catch (error) {
      toast({
        title: "Error",
        description: error instanceof Error ? error.message : "Failed to submit form. Please try again.",
        variant: "destructive",
      });
    }
  };

  return (
    <div className="space-y-4">
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-2">
          <div className="flex gap-2">
            <FormField
              control={form.control}
              name="firstName"
              render={({ field }) => (
                <FormItem>
                  <FormControl>
                    <Input
                      {...field}
                      placeholder="First Name"
                      className="text-sm w-36"
                    />
                  </FormControl>
                </FormItem>
              )}
            />

            <FormField
              control={form.control}
              name="lastName"
              render={({ field }) => (
                <FormItem>
                  <FormControl>
                    <Input
                      {...field}
                      placeholder="Last Name"
                      className="text-sm w-36"
                    />
                  </FormControl>
                </FormItem>
              )}
            />
          </div>

          <div className="flex gap-2 ">
            <FormField
              control={form.control}
              name="company"
              render={({ field }) => (
                <FormItem>
                  <FormControl>
                    <Input
                      {...field}
                      placeholder="Company"
                      className="text-sm w-36"
                    />
                  </FormControl>
                </FormItem>
              )}
            />

            <FormField
              control={form.control}
              name="position"
              render={({ field }) => (
                <FormItem>
                  <FormControl>
                    <Input
                      {...field}
                      placeholder="Position"
                      className="text-sm w-36"
                    />
                  </FormControl>
                </FormItem>
              )}
            />
          </div>

          <div className="flex gap-2">
            <FormField
              control={form.control}
              name="email"
              render={({ field }) => (
                <FormItem>
                  <FormControl>
                    <Input
                      {...field}
                      type="email"
                      placeholder="your.email@company.com"
                      className="text-sm w-48"
                    />
                  </FormControl>
                </FormItem>
              )}
            />

            <Button 
              type="submit" 
              className="" 
              disabled={isDisabled}
              style={{ 
                backgroundColor: isDisabled 
                  ? 'rgba(255, 255, 255, 0.08)' 
                  : 'rgba(255, 255, 255, 0.15)', 
                backdropFilter: isDisabled 
                  ? 'blur(8px)' 
                  : 'blur(12px)' 
              }}
            >
              Declare support
            </Button>
          </div>
          
          <p className="text-xs text-muted-foreground">
            By submitting you accept Merit Capital's{' '}
            <a 
              href="/terms" 
              className="underline underline-offset-4 hover:text-foreground"
            >
              Terms
            </a>
            .
          </p>
        </form>
      </Form>
    </div>
  );
}

