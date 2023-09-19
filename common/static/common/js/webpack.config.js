const path = require('path');
const webpack = require('webpack');


module.exports = {
    entry: {
        common: ['./src/common/index.js']
    },
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: '[name].js',
    },
    plugins: [
        new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery"
        })
    ]
};
