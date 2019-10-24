# web

Line軟體結合市政公車系統 以提供公車查詢功能，不需要另外安裝App，即可查詢公車

[Demo](https://superj80820.github.io/projects/Ahfargo_bus_bot_frontend/#/Bus?RouteID=55)

<img src="https://imgur.com/dMMzZ3v.jpg" width="260">

## 使用技術

* Vue.js: 採用Vue CLI架設SPA架構，前端透過Polling定時向後端Flask拿取公車資料
* Bootstrap-vue: 透過這個組件庫來製作整體前端
* Grid、Flex: 使用此兩種CSS對網頁進行RWD設計 單向資料流的理解: 由於Google Map會在不同Component上顯示，為了讓bug trace更為清楚，所以用vuex來儲存的狀態
* mockjs: 讓前後端分離，開發時可先使用前端自訂Json，除此之外，也可以讓專案在Github demo時不須後端

## Project setup
```
docker-compose run web npm install
```

### Compiles and hot-reloads for development
```
docker-compose up
```

### Compiles and minifies for production
```
docker-compose run web npm run build
```

### Run your tests
```
docker-compose run web npm run test
```

### Lints and fixes files
```
docker-compose run web npm run lint
```

### Run your end-to-end tests
```
docker-compose run web npm run test:e2e
```

### Run your unit tests
```
docker-compose run web npm run test:unit
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
