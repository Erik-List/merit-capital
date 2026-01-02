import { Resend } from 'resend';

const resend = new Resend(process.env.RESEND_API_KEY);

const FROM_EMAIL = process.env.FROM_EMAIL || 'noreply@meritcapit.al';
const FROM_NAME = process.env.FROM_NAME || 'Merit Capital';
const SITE_URL = process.env.NEXT_PUBLIC_SITE_URL || 'https://meritcapit.al';
const LOGO_URL = process.env.LOGO_URL || `${SITE_URL}/icon.svg`;

export async function sendConfirmationEmail({
  email,
  firstName,
  confirmationUrl,
}: {
  email: string;
  firstName: string;
  confirmationUrl: string;
}) {
  try {
    const { data, error } = await resend.emails.send({
      from: `${FROM_NAME} <${FROM_EMAIL}>`,
      to: email,
      subject: 'Confirm your email address',
      html: `
        <!DOCTYPE html>
        <html>
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
          </head>
          <body style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 1.6; color: #0a0a0a; background-color: #fafafa; margin: 0; padding: 0;">
            <table role="presentation" style="width: 100%; border-collapse: collapse; background-color: #fafafa;">
              <tr>
                <td style="padding: 40px 20px;">
                  <table role="presentation" style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 8px; border: 1px solid #e5e7eb; overflow: hidden;">
                    <!-- Header -->
                    <tr>
                      <td style="padding: 40px 40px 30px; text-align: center; border-bottom: 1px solid #f3f4f6;">
                        <img src="${LOGO_URL}" alt="Merit Capital" style="height: 40px; width: auto; margin-bottom: 16px;" />
                        <h1 style="margin: 0; font-size: 24px; font-weight: 400; color: #0a0a0a; letter-spacing: -0.02em;">Welcome to Merit Capital</h1>
                      </td>
                    </tr>
                    <!-- Content -->
                    <tr>
                      <td style="padding: 40px;">
                        <p style="font-size: 16px; line-height: 1.6; margin: 0 0 20px; color: #0a0a0a;">Hi ${firstName},</p>
                        <p style="font-size: 16px; line-height: 1.6; margin: 0 0 32px; color: #374151;">Thank you for supporting Merit Capital. Please confirm your email address to activate your sharing link and start tracking your referrals.</p>
                        
                        <div style="text-align: center; margin: 32px 0;">
                          <a href="${confirmationUrl}" style="display: inline-block; background-color: #0a0a0a; color: #ffffff; padding: 14px 32px; text-decoration: none; border-radius: 6px; font-size: 15px; font-weight: 400; letter-spacing: 0.01em;">Confirm Email Address</a>
                        </div>
                        
                        <p style="font-size: 14px; line-height: 1.5; color: #6b7280; margin: 32px 0 16px;">Or copy and paste this link into your browser:</p>
                        <p style="font-size: 13px; line-height: 1.5; color: #9ca3af; word-break: break-all; margin: 0 0 24px; font-family: 'Monaco', 'Menlo', 'Courier New', monospace;">${confirmationUrl}</p>
                        
                        <p style="font-size: 13px; line-height: 1.5; color: #9ca3af; margin: 0;">This confirmation link will expire in 7 days.</p>
                      </td>
                    </tr>
                    <!-- Footer -->
                    <tr>
                      <td style="padding: 32px 40px; background-color: #fafafa; border-top: 1px solid #f3f4f6;">
                        <p style="font-size: 13px; line-height: 1.5; color: #9ca3af; margin: 0 0 8px;">Best regards,</p>
                        <p style="font-size: 13px; line-height: 1.5; color: #0a0a0a; margin: 0; font-weight: 400;">The Merit Capital Team</p>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </body>
        </html>
      `,
      text: `Hi ${firstName},\n\nThank you for supporting Merit Capital. Please confirm your email address to activate your sharing link and start tracking your referrals.\n\nConfirm your email: ${confirmationUrl}\n\nThis confirmation link will expire in 7 days.\n\nBest regards,\nThe Merit Capital Team`,
    });

    if (error) {
      console.error('Resend error:', error);
      throw new Error(`Failed to send email: ${error.message}`);
    }

    return { success: true, messageId: data?.id };
  } catch (error) {
    console.error('Email sending error:', error);
    throw error;
  }
}

export async function sendSharingLinkEmail({
  email,
  firstName,
  sharingUrl,
  sharingToken,
}: {
  email: string;
  firstName: string;
  sharingUrl: string;
  sharingToken: string;
}) {
  try {
    const { data, error } = await resend.emails.send({
      from: `${FROM_NAME} <${FROM_EMAIL}>`,
      to: email,
      subject: 'Your Merit Capital sharing link is ready',
      html: `
        <!DOCTYPE html>
        <html>
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
          </head>
          <body style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; line-height: 1.6; color: #0a0a0a; background-color: #fafafa; margin: 0; padding: 0;">
            <table role="presentation" style="width: 100%; border-collapse: collapse; background-color: #fafafa;">
              <tr>
                <td style="padding: 40px 20px;">
                  <table role="presentation" style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 8px; border: 1px solid #e5e7eb; overflow: hidden;">
                    <!-- Header -->
                    <tr>
                      <td style="padding: 40px 40px 30px; text-align: center; border-bottom: 1px solid #f3f4f6;">
                        <img src="${LOGO_URL}" alt="Merit Capital" style="height: 40px; width: auto; margin-bottom: 16px;" />
                        <h1 style="margin: 0; font-size: 24px; font-weight: 400; color: #0a0a0a; letter-spacing: -0.02em;">Your sharing link is ready</h1>
                      </td>
                    </tr>
                    <!-- Content -->
                    <tr>
                      <td style="padding: 40px;">
                        <p style="font-size: 16px; line-height: 1.6; margin: 0 0 20px; color: #0a0a0a;">Hi ${firstName},</p>
                        <p style="font-size: 16px; line-height: 1.6; margin: 0 0 32px; color: #374151;">Your email has been confirmed. Your sharing link is now active. Share Merit Capital with your network and track your referrals.</p>
                        
                        <div style="background-color: #f9fafb; border: 1px solid #e5e7eb; border-radius: 6px; padding: 24px; margin: 32px 0;">
                          <p style="font-size: 13px; line-height: 1.5; color: #6b7280; margin: 0 0 12px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.05em;">Your sharing link</p>
                          <p style="font-size: 15px; line-height: 1.5; color: #0a0a0a; word-break: break-all; margin: 0; font-family: 'Monaco', 'Menlo', 'Courier New', monospace; font-weight: 400;">${sharingUrl}</p>
                        </div>

                        <div style="text-align: center; margin: 32px 0;">
                          <a href="${sharingUrl}" style="display: inline-block; background-color: #0a0a0a; color: #ffffff; padding: 14px 32px; text-decoration: none; border-radius: 6px; font-size: 15px; font-weight: 400; letter-spacing: 0.01em;">View Your Link</a>
                        </div>

                        <div style="margin-top: 40px; padding-top: 32px; border-top: 1px solid #f3f4f6;">
                          <p style="font-size: 14px; line-height: 1.5; color: #6b7280; margin: 0 0 16px; text-align: center;">Share on social media</p>
                          <table role="presentation" style="width: 100%; border-collapse: collapse;">
                            <tr>
                              <td style="text-align: center; padding: 0;">
                                <table role="presentation" style="margin: 0 auto; border-collapse: collapse;">
                                  <tr>
                                    <td style="padding: 0 6px;">
                                      <a href="https://wa.me/?text=${encodeURIComponent(`Take a look at Merit Capital - ${sharingUrl}`)}" style="display: inline-block; padding: 10px 20px; background-color: #25D366; color: #ffffff; text-decoration: none; border-radius: 6px; font-size: 14px; font-weight: 400;">WhatsApp</a>
                                    </td>
                                    <td style="padding: 0 6px;">
                                      <a href="https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(sharingUrl)}" style="display: inline-block; padding: 10px 20px; background-color: #0077b5; color: #ffffff; text-decoration: none; border-radius: 6px; font-size: 14px; font-weight: 400;">LinkedIn</a>
                                    </td>
                                    <td style="padding: 0 6px;">
                                      <a href="https://twitter.com/intent/tweet?text=${encodeURIComponent(`Take a look at Merit Capital - ${sharingUrl}`)}" style="display: inline-block; padding: 10px 20px; background-color: #1DA1F2; color: #ffffff; text-decoration: none; border-radius: 6px; font-size: 14px; font-weight: 400;">Twitter</a>
                                    </td>
                                  </tr>
                                </table>
                              </td>
                            </tr>
                          </table>
                        </div>
                      </td>
                    </tr>
                    <!-- Footer -->
                    <tr>
                      <td style="padding: 32px 40px; background-color: #fafafa; border-top: 1px solid #f3f4f6;">
                        <p style="font-size: 13px; line-height: 1.5; color: #9ca3af; margin: 0 0 8px;">Best regards,</p>
                        <p style="font-size: 13px; line-height: 1.5; color: #0a0a0a; margin: 0; font-weight: 400;">The Merit Capital Team</p>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </body>
        </html>
      `,
      text: `Hi ${firstName},\n\nYour email has been confirmed. Your sharing link is now active. Share Merit Capital with your network and track your referrals.\n\nYour sharing link: ${sharingUrl}\n\nBest regards,\nThe Merit Capital Team`,
    });

    if (error) {
      console.error('Resend error:', error);
      throw new Error(`Failed to send email: ${error.message}`);
    }

    return { success: true, messageId: data?.id };
  } catch (error) {
    console.error('Email sending error:', error);
    throw error;
  }
}

