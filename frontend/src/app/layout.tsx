import type { Metadata } from "next";
import "./globals.css";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";


export const metadata: Metadata = {
  title: "Curbside Reservation",
  description: "Curbside reservation app for managing product reservations",
};


export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html
      lang="en"
      className={`h-full antialiased`}
    >
        <body className="min-h-full flex flex-col">{children}</body>
    </html>
  );
}
