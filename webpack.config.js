var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,

  entry: './static/src/course/js/index',

  output: {
      path: path.resolve('./static/src/course/bundles/'),
      filename: "[name].js",
  },

  plugins: [
    new BundleTracker({filename: './course/webpack-stats.json'}),
  ],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      }
    ]
  },
  resolve: {
    extensions: ['*', '.js', '.jsx']
  }

};