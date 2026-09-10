"use client";

import ProductList from "@/components/ProductList";
import { useQuery, useQueryClient, QueryClient, QueryClientProvider } from "@tanstack/react-query";


const queryClient = new QueryClient();


export default function App({ children }: { children: React.ReactNode }) {
  return (
    <QueryClientProvider client={queryClient}>
     <Home/>
    </QueryClientProvider>
  );
}

export function Home() {
  const queryClient = useQueryClient();
  
  // queries the product list
  const productList = useQuery({
    queryKey: ["products"],
    queryFn: async () => {
      const response = await fetch("/api/products");
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    }
  });




  return (
    <div>

      {productList.isLoading && <p>Loading...</p>}
      {productList.isError && <p>Error loading products</p>}
      {productList.data && (
        <ProductList products={productList.data} />
      )}

    </div>
  );
}
