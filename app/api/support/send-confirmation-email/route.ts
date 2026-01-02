import { NextResponse } from 'next/server';
import { sendConfirmationEmail } from '@/lib/email';
import { z } from 'zod';

const emailSchema = z.object({
  email: z.string().email(),
  firstName: z.string().min(1),
  confirmationToken: z.string().min(1),
});

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const data = emailSchema.parse(body);
    
    const confirmationUrl = `${process.env.NEXT_PUBLIC_SITE_URL || 'https://meritcapit.al'}/api/support/confirm-email?token=${data.confirmationToken}`;
    
    await sendConfirmationEmail({
      email: data.email,
      firstName: data.firstName,
      confirmationUrl,
    });
    
    return NextResponse.json({ success: true });
  } catch (error) {
    console.error('Email sending error:', error);
    
    if (error instanceof z.ZodError) {
      return NextResponse.json(
        { error: 'Invalid request data', details: error.errors },
        { status: 400 }
      );
    }
    
    return NextResponse.json(
      { error: 'Failed to send confirmation email' },
      { status: 500 }
    );
  }
}

