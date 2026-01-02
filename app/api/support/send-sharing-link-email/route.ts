import { NextResponse } from 'next/server';
import { sendSharingLinkEmail } from '@/lib/email';
import { z } from 'zod';

const emailSchema = z.object({
  email: z.string().email(),
  firstName: z.string().min(1),
  sharingToken: z.string().min(1),
});

export async function POST(request: Request) {
  try {
    const body = await request.json();
    const data = emailSchema.parse(body);
    
    const sharingUrl = `${process.env.NEXT_PUBLIC_SITE_URL || 'https://meritcapit.al'}/shared-by/${data.sharingToken}`;
    
    await sendSharingLinkEmail({
      email: data.email,
      firstName: data.firstName,
      sharingUrl,
      sharingToken: data.sharingToken,
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
      { error: 'Failed to send sharing link email' },
      { status: 500 }
    );
  }
}

