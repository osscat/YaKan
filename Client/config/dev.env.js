'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  SERVER_ADDRESS: '"localhost:8000"',
  API_BASE_URL: '"http://127.0.0.1:8000"'
})
