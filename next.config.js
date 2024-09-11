// /** @type {import('next').NextConfig} */
// const nextConfig = {}

// module.exports = nextConfig

// next.config.js
module.exports = {
    reactStrictMode: true,
    exportPathMap: async function (
        defaultPathMap,
        { dev, dir, outDir, distDir, buildId }
    ) {
        return {
            '/': { page: '/' },
            // добавьте другие страницы, если они есть
        }
    }
}