"use client"

import { useState } from 'react'
import { useRouter } from 'next/navigation'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '@/components/ui/card'
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/components/ui/form'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'
import { Textarea } from '@/components/ui/textarea'
import { Slider } from '@/components/ui/slider'
import { zodResolver } from '@hookform/resolvers/zod'
import { useForm } from 'react-hook-form'
import * as z from 'zod'
import { Search } from 'lucide-react'
import { useToast } from '@/hooks/use-toast'

// Define the Investor type
interface Investor {
  id: string
  name: string
  logo_url: string
  hq_location: string
}

const formSchema = z.object({
  investorId: z.string().min(1, 'Please select an investor'),
  integrityScore: z.number().min(1).max(10),
  operationalSupportScore: z.number().min(1).max(10),
  fundraisingSupportScore: z.number().min(1).max(10),
  responsivenessScore: z.number().min(1).max(10),
  comments: z.string().min(10, 'Please provide more detailed feedback'),
  stageOfCompany: z.string().min(1, 'Please select your company stage'),
  positionOfFounder: z.string().min(1, 'Please select your position'),
})

export function RateForm() {
  const router = useRouter()
  const { toast } = useToast()
  const [searchQuery, setSearchQuery] = useState('')
  const [selectedInvestor, setSelectedInvestor] = useState<Investor | null>(null)
  const [searchResults, setSearchResults] = useState<Investor[]>([])

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      integrityScore: 5,
      operationalSupportScore: 5,
      fundraisingSupportScore: 5,
      responsivenessScore: 5,
      comments: '',
    },
  })

  const filteredInvestors = searchResults.filter(investor =>
    investor.name.toLowerCase().includes(searchQuery.toLowerCase())
  )

  const onSubmit = async (values: z.infer<typeof formSchema>) => {
    if (!selectedInvestor) return

    // Calculate overall rating
    const overallRating = (
      values.integrityScore +
      values.operationalSupportScore +
      values.fundraisingSupportScore +
      values.responsivenessScore
    ) / 4

    try {
      // TODO: Implement actual rating submission
      router.push('/logs')
    } catch (error) {
      toast({
        title: "Error submitting rating",
        description: "Please try again later",
        variant: "destructive",
      })
    }
  }

  return (
    <>
      <Card>
        <CardHeader>
          <CardTitle>Select Investor</CardTitle>
          <CardDescription>
            Search for the investor you want to rate
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="relative">
            <Search className="absolute left-3 top-3 h-4 w-4 text-muted-foreground" />
            <Input
              placeholder="Search investors..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="pl-9"
            />
          </div>
          {searchQuery && (
            <div className="mt-4 space-y-2">
              {filteredInvestors.map((investor) => (
                <div
                  key={investor.id}
                  className={`flex items-center gap-3 p-3 rounded-lg hover:bg-accent/10 cursor-pointer ${
                    selectedInvestor?.id === investor.id ? 'bg-accent' : ''
                  }`}
                  onClick={() => {
                    setSelectedInvestor(investor)
                    form.setValue('investorId', String(investor.id))
                  }}
                >
                  <img
                    src={investor.logo_url}
                    alt={investor.name}
                    className="w-8 h-8 rounded-full"
                  />
                  <div>
                    <div className="font-medium">{investor.name}</div>
                    <div className="text-sm text-muted-foreground">
                      {investor.hq_location}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </CardContent>
      </Card>

      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
          <FormField
            control={form.control}
            name="integrityScore"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Integrity & Conviction</FormLabel>
                <FormControl>
                  <div className="space-y-3">
                    <Slider
                      min={1}
                      max={10}
                      step={1}
                      value={[field.value]}
                      onValueChange={(value) => field.onChange(value[0])}
                    />
                    <div className="text-center font-medium">
                      {field.value} / 10
                    </div>
                  </div>
                </FormControl>
                <FormDescription>
                  Rate the investor&apos;s integrity and conviction in supporting portfolio companies
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            control={form.control}
            name="operationalSupportScore"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Operational Support</FormLabel>
                <FormControl>
                  <div className="space-y-3">
                    <Slider
                      min={1}
                      max={10}
                      step={1}
                      value={[field.value]}
                      onValueChange={(value) => field.onChange(value[0])}
                    />
                    <div className="text-center font-medium">
                      {field.value} / 10
                    </div>
                  </div>
                </FormControl>
                <FormDescription>
                  Rate the quality of operational support and guidance provided
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            control={form.control}
            name="fundraisingSupportScore"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Fundraising Support</FormLabel>
                <FormControl>
                  <div className="space-y-3">
                    <Slider
                      min={1}
                      max={10}
                      step={1}
                      value={[field.value]}
                      onValueChange={(value) => field.onChange(value[0])}
                    />
                    <div className="text-center font-medium">
                      {field.value} / 10
                    </div>
                  </div>
                </FormControl>
                <FormDescription>
                  Rate the investor&apos;s support in subsequent fundraising efforts
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            control={form.control}
            name="responsivenessScore"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Responsiveness</FormLabel>
                <FormControl>
                  <div className="space-y-3">
                    <Slider
                      min={1}
                      max={10}
                      step={1}
                      value={[field.value]}
                      onValueChange={(value) => field.onChange(value[0])}
                    />
                    <div className="text-center font-medium">
                      {field.value} / 10
                    </div>
                  </div>
                </FormControl>
                <FormDescription>
                  Rate how responsive and accessible the investor is
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            control={form.control}
            name="comments"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Comments</FormLabel>
                <FormControl>
                  <Textarea
                    placeholder="Share your experience working with this investor..."
                    className="min-h-[100px]"
                    {...field}
                  />
                </FormControl>
                <FormDescription>
                  Provide detailed feedback about your experience
                </FormDescription>
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            control={form.control}
            name="stageOfCompany"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Company Stage</FormLabel>
                <Select onValueChange={field.onChange} defaultValue={field.value}>
                  <FormControl>
                    <SelectTrigger>
                      <SelectValue placeholder="Select your company stage" />
                    </SelectTrigger>
                  </FormControl>
                  <SelectContent>
                    <SelectItem value="pre-seed">Pre-seed</SelectItem>
                    <SelectItem value="seed">Seed</SelectItem>
                    <SelectItem value="series a">Series A</SelectItem>
                    <SelectItem value="series b">Series B</SelectItem>
                    <SelectItem value="other">Other</SelectItem>
                  </SelectContent>
                </Select>
                <FormMessage />
              </FormItem>
            )}
          />

          <FormField
            control={form.control}
            name="positionOfFounder"
            render={({ field }) => (
              <FormItem>
                <FormLabel>Your Position</FormLabel>
                <Select onValueChange={field.onChange} defaultValue={field.value}>
                  <FormControl>
                    <SelectTrigger>
                      <SelectValue placeholder="Select your position" />
                    </SelectTrigger>
                  </FormControl>
                  <SelectContent>
                    <SelectItem value="CEO">CEO</SelectItem>
                    <SelectItem value="CTO">CTO</SelectItem>
                    <SelectItem value="COO">COO</SelectItem>
                    <SelectItem value="other">Other</SelectItem>
                  </SelectContent>
                </Select>
                <FormMessage />
              </FormItem>
            )}
          />

          <Button 
            type="submit" 
            size="lg" 
            className="w-full"
            disabled={!selectedInvestor}
          >
            Submit Rating
          </Button>
        </form>
      </Form>
    </>
  )
} 