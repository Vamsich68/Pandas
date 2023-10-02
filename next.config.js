/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  exportTrailingSlash: true,
  trailingSlash: true,
  experimental: {
    appDir: true,
  },
};

module.exports = nextConfig;
