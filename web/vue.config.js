module.exports = {
  devServer: {
    proxy: process.env.NODE_ENV === 'messfarDev'
    ? 'https://messfar.com/dev/ahfargo/web/'
    : "http://app:8090/",
    disableHostCheck: true
  },
  publicPath: process.env.NODE_ENV === 'messfarDev'
    ? '/dev/ahfargo/web/'
    : '/'
};
