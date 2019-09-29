module.exports = {
  devServer: {
    proxy: "http://messfar.com/dev/ahfargo/web/",
    disableHostCheck: true
  },
  publicPath: process.env.NODE_ENV === 'messfarDev'
    ? '/dev/ahfargo/web/'
    : '/'
};
