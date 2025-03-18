import Link from 'next/link';
import { ArrowRight } from 'lucide-react';

export default function IdeaValidationPage() {
  return (
    <div className="min-h-screen bg-background flex items-center justify-center p-4">
      <div className="max-w-xl w-full space-y-6">
        <h1 className="text-2xl font-semibold text-center mb-8">
          Select a Version
        </h1>
        
        <Link 
          href="/idea-validation/marketing-angle-1"
          className="block p-6 bg-card hover:bg-accent rounded-lg border transition-colors duration-200"
        >
          <div className="flex items-center justify-between">
            <div>
              <h2 className="text-xl font-medium mb-2">Marketing Angle 1</h2>
              <p className="text-muted-foreground">Version focused on transparency and trust</p>
            </div>
            <ArrowRight className="h-5 w-5 text-muted-foreground" />
          </div>
        </Link>

        <Link 
          href="/idea-validation/marketing-angle-2"
          className="block p-6 bg-card hover:bg-accent rounded-lg border transition-colors duration-200"
        >
          <div className="flex items-center justify-between">
            <div>
              <h2 className="text-xl font-medium mb-2">Marketing Angle 2</h2>
              <p className="text-muted-foreground">Version focused on community and collaboration</p>
            </div>
            <ArrowRight className="h-5 w-5 text-muted-foreground" />
          </div>
        </Link>

        <Link 
          href="/idea-validation/marketing-angle-3"
          className="block p-6 bg-card hover:bg-accent rounded-lg border transition-colors duration-200"
        >
          <div className="flex items-center justify-between">
            <div>
              <h2 className="text-xl font-medium mb-2">Marketing Angle 3</h2>
              <p className="text-muted-foreground">Version focused on data-driven decisions</p>
            </div>
            <ArrowRight className="h-5 w-5 text-muted-foreground" />
          </div>
        </Link>
      </div>
    </div>
  );
} 