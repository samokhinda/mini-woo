// /** @type {import('next').NextConfig} */
// const nextConfig = {}

// module.exports = nextConfig

// next.config.js
// const nextConfig = {
//     reactStrictMode: true,
//     exportPathMap: async function (
//         defaultPathMap,
//         { dev, dir, outDir, distDir, buildId }
//     ) {
//         return {
//             '/': { page: '/' },
//             // Добавьте другие страницы, если они присутствуют
//         }
//     }
// }

// module.exports = nextConfig

// next.config.js
// const nextConfig = {
//     reactStrictMode: true,
//     // Удалено exportPathMap
// }

// module.exports = nextConfig;

// /** @type {import('next').NextConfig} */
// const nextConfig = {
//     distDir: 'out',
//   }
  
//   module.exports = nextConfig

// /** @type {import('next').NextConfig} */
// const nextConfig = {
//     distDir: 'out',
//     exportPathMap: async function (
//       defaultPathMap,
//       { dev, dir, outDir, distDir, buildId }
//     ) {
//       return {
//         '/': { page: '/' },
//       };
//     },
//   };
  
//   module.exports = nextConfig;

/** @type {import('next').NextConfig} */
const nextConfig = {
    distDir: 'out',
  };
  
  module.exports = nextConfig;