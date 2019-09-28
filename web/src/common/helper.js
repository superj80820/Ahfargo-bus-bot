const helper = {
  retryPomise(max, interval, func) {
    // Ref: https://stackoverflow.com/questions/38213668/promise-retry-design-patterns
    function _rejectDelay(interval) {
      return (function(reason) {
        return new Promise(function(_, reject) {
          setTimeout(reject.bind(null, reason), interval);
        });
      })();
    }
    let p = Promise.reject();
    for (let i = 0; i < max; i++) {
      p = p.catch(func).catch(() => _rejectDelay(interval));
    }
    return p;
  }
};

export default helper;
