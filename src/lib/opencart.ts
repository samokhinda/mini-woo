// lib/opencart.ts

const OPENCART_URL = process.env.OPENCART_URL!!
const API_KEY = process.env.OPENCART_API_KEY!!

function call(method: string, api: string, query?: URLSearchParams, body?: any) {
    const headers = {
        "Content-Type": "application/json",
        "API-Key": API_KEY
    };

    let url = `${OPENCART_URL}/index.php?route=${api}`.replace("//", "/");
    if (query) {
        url = `${url}&${query.toString()}`;
    }

    const init = { method, headers };
    if (body) {
        init.body = JSON.stringify(body);
    }

    return fetch(url, init);
}

export function get(api: string, query?: URLSearchParams) {
    return call("GET", api, query);
}

export function post(api: string, body: any, query?: URLSearchParams) {
    return call("POST", api, query, body);
}

export function put(api: string, body: any, query?: URLSearchParams) {
    return call("PUT", api, query, body);
}