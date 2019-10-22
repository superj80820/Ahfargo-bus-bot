module.exports = {
  devServer: process.env.VUE_APP_MOCK_SERVER !== "true" ? {
    proxy: "http://app:8090/",
    disableHostCheck: true
  } : {},
  publicPath: process.env.VUE_APP_BASE_URL !== "" ? process.env.VUE_APP_BASE_URL : "/"
};
