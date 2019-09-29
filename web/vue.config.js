module.exports = {
  devServer: {
    proxy: "http://app:8090/",
    disableHostCheck: true
  },
  publicPath: process.env.NODE_ENV === 'messfarDev'
    ? '/dev/ahfargo/web/'
    : '/'
};
