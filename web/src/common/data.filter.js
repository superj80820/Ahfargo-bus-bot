const dataFilter = {
  format(time) {
    time = time.toString();
    if (time.match(/T(\d+:\d+)/) !== null) {
      // e.g: 2019-09-26T20:12:00+08:00 to 20:12
      return time.match(/T(\d+:\d+)/)[1];
    }
    if (time.match(/\d+/) !== null) {
      // sec to min. e.g: 120 to 2
      return time / 60;
    }
    console.error("dataFilter format error!");
  }
};

export default dataFilter;
