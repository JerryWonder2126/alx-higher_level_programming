#!/usr/bin/node

const callMeMoby = (freq, callback) => {
  while (freq) {
    callback();
    freq = freq - 1;
  }
};

module.exports = { callMeMoby };
