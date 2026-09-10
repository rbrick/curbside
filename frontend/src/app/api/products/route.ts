import { env } from "process";


export async function GET() {
    console.log(`Fetching products from ${env.API_URL}/products`);
    const resp = await fetch(`${env.API_URL}/products`);
    return resp;

}