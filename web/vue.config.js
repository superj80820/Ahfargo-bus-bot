module.exports = {
  devServer: {
    proxy: "http://app:5010/",
    disableHostCheck: true
  },
  publicPath: process.env.NODE_ENV === 'messfarDev'
    ? '/dev/ahfargo/web/'
    : '/'
};
