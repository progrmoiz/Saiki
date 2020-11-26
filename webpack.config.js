var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');


const COMPONENT_DIR = path.resolve(__dirname, 'static', 'components')
const STATIC_DIR = path.resolve(__dirname, 'static', 'course', 'js');
const SOURCE_DIR = path.resolve(STATIC_DIR, 'src');

module.exports = {
  mode: "production",
  devtool: 'source-map',
  entry: {
    plugin: path.resolve(SOURCE_DIR, 'index.js')
  },
  output: {
    filename: `[name]-[hash].js`,
    path: STATIC_DIR,
    publicPath: ''
  },
  optimization: {
    splitChunks: {
      cacheGroups: {
        default: false,
        vendors: false,
        vendor: {
          name: 'vendors',
          chunks: 'all',
          test: /node_modules/
        }
      }
    },
    minimize: true
  },
  plugins: [
    new BundleTracker({
			path: STATIC_DIR,
			filename: "./webpack-stats.json"
		})
  ],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      }
    ]
  },
  resolve: {
    alias: {
      components: COMPONENT_DIR,
    },
    extensions: ['*', '.js', '.jsx']
  },
  externals: {
    react: 'React',
    'react-dom': 'ReactDOM'
  }
};