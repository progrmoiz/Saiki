var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');


const COMPONENT_DIR = path.resolve(__dirname, 'static', 'components')
const STATIC_DIR = path.resolve(__dirname, 'static');
const COURSE_SOURCE_DIR = path.resolve(STATIC_DIR, 'course', 'js', 'src');
const ASSIGNMENT_SOURCE_DIR = path.resolve(STATIC_DIR, 'assignment', 'js', 'src');

module.exports = {
  mode: "production",
  devtool: 'source-map',
  entry: {
    course: path.resolve(COURSE_SOURCE_DIR, 'index.js'),
    assignment: path.resolve(ASSIGNMENT_SOURCE_DIR, 'index.js'),
  },
  output: {
    filename: `[name]-1.0.0.js`,
    path: path.resolve(STATIC_DIR, 'bundles'),
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
			path: path.resolve(STATIC_DIR, 'bundles'),
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