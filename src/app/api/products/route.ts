import {NextRequest, NextResponse} from "next/server";
import woo from "@/lib/woo";

export async function GET(request: NextRequest) {
    const params = request.nextUrl.searchParams
    params.set('status', 'publish')
    const res = await woo.get('products', params)
    return NextResponse.json(await res.json())
}

// /api/products/route.ts

// import { NextRequest, NextResponse } from 'next/server';
// import { get as getOpenCart } from '@/lib/opencart';

// export async function GET(request: NextRequest) {
//     const params = request.nextUrl.searchParams;
//     params.set('status', 'publish');
//     const res = await getOpenCart('api/product/getProducts', params);
//     return NextResponse.json(await res.json());
// }