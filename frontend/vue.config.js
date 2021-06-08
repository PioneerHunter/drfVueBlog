const path = require("path");

module.exports = {
  devServer: {
    // 代理，解决跨域
    proxy: {
      "/api": {
        target: "http://127.0.0.1:8000/api",
        changeOrigin: true,
        pathRewrite: {
          "/api": "",
        },
      },
    },
  },
  pluginOptions: {
    "style-resources-loader": {
      preProcessor: "less",
      patterns: [
        path.resolve(__dirname, "./src/assets/style/lessStyle.less"), // 全局引入less文件
      ],
    },
  },
};
