import Mock from "mockjs";

export function mock() {
  Mock.mock(new RegExp('v2/Bus/EstimatedTimeOfArrival/City/Taichung/55.*'), [
    {
      StopName: {
        Zh_tw: "光明國中(貴和街)",
        En: "Guang Ming Junior High School(Guei Han Street)"
      },
      Direction: 0,
      StopSequence: 1,
      StopStatus: 1,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:35:00+08:00",
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "豐原",
        En: "Fengyuan"
      },
      Direction: 1,
      StopSequence: 1,
      StopStatus: 1,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:35:00+08:00",
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "媽祖廟",
        En: "Mazu Temple"
      },
      Direction: 1,
      StopSequence: 2,
      StopStatus: 1,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:36:00+08:00",
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "臺中刑務所演武場",
        En: "Budokan Martial Arts Hall"
      },
      Direction: 0,
      StopSequence: 2,
      StopStatus: 1,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:35:00+08:00",
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "臺灣企銀(豐原郵局)",
        En: "Taiwan Business Bank (Fengyuan Post Office)"
      },
      Direction: 1,
      StopSequence: 3,
      StopStatus: 1,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:38:00+08:00",
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "地方法院",
        En: "Taichung District Court"
      },
      Direction: 0,
      EstimateTime: 180,
      StopSequence: 3,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:37:00+08:00",
      Estimates: [
        {
          PlateNumb: "016-FV",
          EstimateTime: 180,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "臺中女中",
        En: "Taichung Girls Senior High School"
      },
      Direction: 0,
      EstimateTime: 180,
      StopSequence: 4,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:38:00+08:00",
      Estimates: [
        {
          PlateNumb: "016-FV",
          EstimateTime: 180,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "電信局",
        En: "Telecom Company"
      },
      Direction: 1,
      StopSequence: 4,
      StopStatus: 1,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:39:00+08:00",
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "豐原高商",
        En: "Fengyuan Voc. School"
      },
      Direction: 1,
      EstimateTime: 0,
      StopSequence: 5,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:40:00+08:00",
      Estimates: [
        {
          PlateNumb: "FAE-757",
          EstimateTime: 0,
          IsLastBus: false,
          VehicleStopStatus: 1
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "民權繼光街口",
        En: "Minquan-Jiguang Intersection"
      },
      Direction: 0,
      EstimateTime: 240,
      StopSequence: 5,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:39:00+08:00",
      Estimates: [
        {
          PlateNumb: "016-FV",
          EstimateTime: 240,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "豐原分局",
        En: "Fengyuan Police Office"
      },
      Direction: 1,
      EstimateTime: 120,
      StopSequence: 6,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:42:00+08:00",
      Estimates: [
        {
          PlateNumb: "FAE-757",
          EstimateTime: 120,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "臺中車站(民族路口)",
        En: "Taichung Station(Minzu Rd. Intersection)"
      },
      Direction: 0,
      EstimateTime: 360,
      StopSequence: 6,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:41:00+08:00",
      Estimates: [
        {
          PlateNumb: "016-FV",
          EstimateTime: 360,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "干城站",
        En: "Gancheng Station"
      },
      Direction: 0,
      EstimateTime: 120,
      StopSequence: 7,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:44:00+08:00",
      Estimates: [
        {
          PlateNumb: "709-FX",
          EstimateTime: 120,
          IsLastBus: false
        },
        {
          PlateNumb: "016-FV",
          EstimateTime: 540,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "輸配電",
        En: "Power Distribution"
      },
      Direction: 1,
      EstimateTime: 180,
      StopSequence: 7,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:42:00+08:00",
      Estimates: [
        {
          PlateNumb: "FAE-757",
          EstimateTime: 180,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "文化新村",
        En: "Cultural Community"
      },
      Direction: 1,
      EstimateTime: 180,
      StopSequence: 8,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:44:00+08:00",
      Estimates: [
        {
          PlateNumb: "FAE-757",
          EstimateTime: 180,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "臺中公園(雙十路)",
        En: "Taichung Park (Shuangshi Rd.)"
      },
      Direction: 0,
      EstimateTime: 180,
      StopSequence: 8,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:45:00+08:00",
      Estimates: [
        {
          PlateNumb: "709-FX",
          EstimateTime: 180,
          IsLastBus: false
        },
        {
          PlateNumb: "016-FV",
          EstimateTime: 600,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "菸廠",
        En: "Tobacco Factory"
      },
      Direction: 1,
      EstimateTime: 240,
      StopSequence: 9,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:45:00+08:00",
      Estimates: [
        {
          PlateNumb: "FAE-757",
          EstimateTime: 240,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "中興堂",
        En: "Chunghsing Hall"
      },
      Direction: 0,
      EstimateTime: 300,
      StopSequence: 9,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:47:00+08:00",
      Estimates: [
        {
          PlateNumb: "709-FX",
          EstimateTime: 300,
          IsLastBus: false
        },
        {
          PlateNumb: "016-FV",
          EstimateTime: 720,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "國立臺中科技大學",
        En: "National Taichung University of Science and Technology"
      },
      Direction: 0,
      EstimateTime: 480,
      StopSequence: 10,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:50:00+08:00",
      Estimates: [
        {
          PlateNumb: "709-FX",
          EstimateTime: 480,
          IsLastBus: false
        },
        {
          PlateNumb: "016-FV",
          EstimateTime: 900,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "栗林車站",
        En: "Lilin Station"
      },
      Direction: 1,
      EstimateTime: 240,
      StopSequence: 10,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:45:00+08:00",
      Estimates: [
        {
          PlateNumb: "FAE-757",
          EstimateTime: 240,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "中友百貨",
        En: "Chungyo Department Store"
      },
      Direction: 0,
      EstimateTime: 480,
      StopSequence: 11,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:51:00+08:00",
      Estimates: [
        {
          PlateNumb: "709-FX",
          EstimateTime: 480,
          IsLastBus: false
        },
        {
          PlateNumb: "016-FV",
          EstimateTime: 960,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "校栗林",
        En: "Xiaolilin"
      },
      Direction: 1,
      EstimateTime: 300,
      StopSequence: 11,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:46:00+08:00",
      Estimates: [
        {
          PlateNumb: "FAE-757",
          EstimateTime: 300,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "一心市場",
        En: "Yixin Market"
      },
      Direction: 0,
      EstimateTime: 540,
      StopSequence: 12,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:52:00+08:00",
      Estimates: [
        {
          PlateNumb: "709-FX",
          EstimateTime: 540,
          IsLastBus: false
        },
        {
          PlateNumb: "016-FV",
          EstimateTime: 1020,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "中山祥和路口",
        En: "Zhongshan-Xianghe Intersection"
      },
      Direction: 1,
      EstimateTime: 360,
      StopSequence: 12,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:47:00+08:00",
      Estimates: [
        {
          PlateNumb: "FAE-757",
          EstimateTime: 360,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "弘文中學",
        En: "Hongwen Junior High School"
      },
      Direction: 1,
      EstimateTime: 420,
      StopSequence: 13,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:47:00+08:00",
      Estimates: [
        {
          PlateNumb: "FAE-757",
          EstimateTime: 420,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "三民錦中街口",
        En: "Sanmin-Jinzhong Intersection"
      },
      Direction: 0,
      EstimateTime: 600,
      StopSequence: 13,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:53:00+08:00",
      Estimates: [
        {
          PlateNumb: "709-FX",
          EstimateTime: 600,
          IsLastBus: false
        },
        {
          PlateNumb: "016-FV",
          EstimateTime: 1080,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "矽品精密",
        En: "S.P.I.L."
      },
      Direction: 1,
      EstimateTime: 420,
      StopSequence: 14,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:48:00+08:00",
      Estimates: [
        {
          PlateNumb: "FAE-757",
          EstimateTime: 420,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "新民高中(三民路)",
        En: "Shin-min Senior High School(Sanmin Rd.)"
      },
      Direction: 0,
      EstimateTime: 660,
      StopSequence: 14,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:54:00+08:00",
      Estimates: [
        {
          PlateNumb: "709-FX",
          EstimateTime: 660,
          IsLastBus: false
        },
        {
          PlateNumb: "016-FV",
          EstimateTime: 1080,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "潭秀里",
        En: "Tanxiu Village"
      },
      Direction: 1,
      EstimateTime: 480,
      StopSequence: 15,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:49:00+08:00",
      Estimates: [
        {
          PlateNumb: "FAE-757",
          EstimateTime: 480,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    },
    {
      StopName: {
        Zh_tw: "寶覺寺",
        En: "Baojue Temple"
      },
      Direction: 0,
      EstimateTime: 720,
      StopSequence: 15,
      StopStatus: 0,
      MessageType: 0,
      NextBusTime: "2019-10-22T07:54:00+08:00",
      Estimates: [
        {
          PlateNumb: "709-FX",
          EstimateTime: 720,
          IsLastBus: false
        },
        {
          PlateNumb: "016-FV",
          EstimateTime: 1140,
          IsLastBus: false
        }
      ],
      SrcUpdateTime: "2019-10-22T07:26:10+08:00",
      UpdateTime: "2019-10-22T07:27:18+08:00"
    }
  ]);
  Mock.mock(new RegExp('v2/Bus/StopOfRoute/City/Taichung/55.*'), [
    {
      Direction: 0,
      Stops: [
        {
          StopUID: "TXG10005",
          StopID: "10005",
          StopName: {
            Zh_tw: "光明國中(貴和街)",
            En: "Guang Ming Junior High School(Guei Han Street)"
          },
          StopBoarding: 0,
          StopSequence: 1,
          StopPosition: {
            PositionLat: 24.133201,
            PositionLon: 120.674334
          },
          StationNameID: "4091",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG20748",
          StopID: "20748",
          StopName: {
            Zh_tw: "臺中刑務所演武場",
            En: "Budokan Martial Arts Hall"
          },
          StopBoarding: 0,
          StopSequence: 2,
          StopPosition: {
            PositionLat: 24.134358,
            PositionLon: 120.673256
          },
          StationNameID: "6212",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13306",
          StopID: "13306",
          StopName: {
            Zh_tw: "地方法院",
            En: "Taichung District Court"
          },
          StopBoarding: 0,
          StopSequence: 3,
          StopPosition: {
            PositionLat: 24.134044,
            PositionLon: 120.675885
          },
          StationNameID: "0070",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13288",
          StopID: "13288",
          StopName: {
            Zh_tw: "臺中女中",
            En: "Taichung Girls Senior High School"
          },
          StopBoarding: 0,
          StopSequence: 4,
          StopPosition: {
            PositionLat: 24.135958,
            PositionLon: 120.678025
          },
          StationNameID: "0071",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13343",
          StopID: "13343",
          StopName: {
            Zh_tw: "民權繼光街口",
            En: "Minquan-Jiguang Intersection"
          },
          StopBoarding: 0,
          StopSequence: 5,
          StopPosition: {
            PositionLat: 24.137009,
            PositionLon: 120.681009
          },
          StationNameID: "4284",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG7352",
          StopID: "7352",
          StopName: {
            Zh_tw: "臺中車站(民族路口)",
            En: "Taichung Station(Minzu Rd. Intersection)"
          },
          StopBoarding: 0,
          StopSequence: 6,
          StopPosition: {
            PositionLat: 24.136519,
            PositionLon: 120.683912
          },
          StationNameID: "6510",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13253",
          StopID: "13253",
          StopName: {
            Zh_tw: "干城站",
            En: "Gancheng Station"
          },
          StopBoarding: 0,
          StopSequence: 7,
          StopPosition: {
            PositionLat: 24.140888,
            PositionLon: 120.685985
          },
          StationNameID: "0402",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13289",
          StopID: "13289",
          StopName: {
            Zh_tw: "臺中公園(雙十路)",
            En: "Taichung Park (Shuangshi Rd.)"
          },
          StopBoarding: 0,
          StopSequence: 8,
          StopPosition: {
            PositionLat: 24.1439927651,
            PositionLon: 120.686123371
          },
          StationNameID: "4544",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG16189",
          StopID: "16189",
          StopName: {
            Zh_tw: "中興堂",
            En: "Chunghsing Hall"
          },
          StopBoarding: 0,
          StopSequence: 9,
          StopPosition: {
            PositionLat: 24.146258,
            PositionLon: 120.684481
          },
          StationNameID: "1513",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13293",
          StopID: "13293",
          StopName: {
            Zh_tw: "國立臺中科技大學",
            En: "National Taichung University of Science and Technology"
          },
          StopBoarding: 0,
          StopSequence: 10,
          StopPosition: {
            PositionLat: 24.149867,
            PositionLon: 120.68413
          },
          StationNameID: "0045",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13255",
          StopID: "13255",
          StopName: {
            Zh_tw: "中友百貨",
            En: "Chungyo Department Store"
          },
          StopBoarding: 0,
          StopSequence: 11,
          StopPosition: {
            PositionLat: 24.15251,
            PositionLon: 120.685197
          },
          StationNameID: "0046",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13251",
          StopID: "13251",
          StopName: {
            Zh_tw: "一心市場",
            En: "Yixin Market"
          },
          StopBoarding: 0,
          StopSequence: 12,
          StopPosition: {
            PositionLat: 24.153663,
            PositionLon: 120.685713
          },
          StationNameID: "0047",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG1459",
          StopID: "1459",
          StopName: {
            Zh_tw: "三民錦中街口",
            En: "Sanmin-Jinzhong Intersection"
          },
          StopBoarding: 0,
          StopSequence: 13,
          StopPosition: {
            PositionLat: 24.1552783333333,
            PositionLon: 120.68695
          },
          StationNameID: "0934",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13322",
          StopID: "13322",
          StopName: {
            Zh_tw: "新民高中(三民路)",
            En: "Shin-min Senior High School(Sanmin Rd.)"
          },
          StopBoarding: 0,
          StopSequence: 14,
          StopPosition: {
            PositionLat: 24.156805,
            PositionLon: 120.688503
          },
          StationNameID: "4399",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13342",
          StopID: "13342",
          StopName: {
            Zh_tw: "寶覺寺",
            En: "Baojue Temple"
          },
          StopBoarding: 0,
          StopSequence: 15,
          StopPosition: {
            PositionLat: 24.158027,
            PositionLon: 120.689922
          },
          StationNameID: "0960",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13326",
          StopID: "13326",
          StopName: {
            Zh_tw: "監理站",
            En: "Motor Vehicles Office"
          },
          StopBoarding: 0,
          StopSequence: 16,
          StopPosition: {
            PositionLat: 24.161057,
            PositionLon: 120.69209
          },
          StationNameID: "0892",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13346",
          StopID: "13346",
          StopName: {
            Zh_tw: "北屯國小(北屯路)",
            En: "Beitun Elementary School(Beitun Rd.)"
          },
          StopBoarding: 0,
          StopSequence: 17,
          StopPosition: {
            PositionLat: 24.16325,
            PositionLon: 120.69318
          },
          StationNameID: "5405",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13283",
          StopID: "13283",
          StopName: {
            Zh_tw: "北屯",
            En: "Beitun"
          },
          StopBoarding: 0,
          StopSequence: 18,
          StopPosition: {
            PositionLat: 24.165043,
            PositionLon: 120.694182
          },
          StationNameID: "0492",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13259",
          StopID: "13259",
          StopName: {
            Zh_tw: "三光國中",
            En: "Sanguang junior high school"
          },
          StopBoarding: 0,
          StopSequence: 19,
          StopPosition: {
            PositionLat: 24.167619,
            PositionLon: 120.695909
          },
          StationNameID: "5511",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13284",
          StopID: "13284",
          StopName: {
            Zh_tw: "大坑口",
            En: "Dakengkou"
          },
          StopBoarding: 0,
          StopSequence: 20,
          StopPosition: {
            PositionLat: 24.169732,
            PositionLon: 120.697165
          },
          StationNameID: "0103",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG17946",
          StopID: "17946",
          StopName: {
            Zh_tw: "北屯文心路口",
            En: "Beitun-Wenxin Rd. Intersection"
          },
          StopBoarding: 0,
          StopSequence: 21,
          StopPosition: {
            PositionLat: 24.17061,
            PositionLon: 120.697915
          },
          StationNameID: "4951",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13314",
          StopID: "13314",
          StopName: {
            Zh_tw: "特力屋北屯店",
            En: "B&Q Beitun Branch"
          },
          StopBoarding: 0,
          StopSequence: 22,
          StopPosition: {
            PositionLat: 24.173743,
            PositionLon: 120.698344
          },
          StationNameID: "0364",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13299",
          StopID: "13299",
          StopName: {
            Zh_tw: "北屯崇德二路口",
            En: "Beitun-Chongde 2nd Intersection"
          },
          StopBoarding: 0,
          StopSequence: 23,
          StopPosition: {
            PositionLat: 24.175848,
            PositionLon: 120.699317
          },
          StationNameID: "0200",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13286",
          StopID: "13286",
          StopName: {
            Zh_tw: "北新國中",
            En: "Beixin Junior High School"
          },
          StopBoarding: 0,
          StopSequence: 24,
          StopPosition: {
            PositionLat: 24.17842,
            PositionLon: 120.700337
          },
          StationNameID: "0105",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG2232",
          StopID: "2232",
          StopName: {
            Zh_tw: "捷運松竹站(北屯路)",
            En: "MRT Songzhu Station(Beitun Rd.)"
          },
          StopBoarding: 0,
          StopSequence: 25,
          StopPosition: {
            PositionLat: 24.182616,
            PositionLon: 120.702086
          },
          StationNameID: "6464",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13325",
          StopID: "13325",
          StopName: {
            Zh_tw: "中山路一巷口",
            En: "Zhongshan Rd. 1st. Ln. Intersection"
          },
          StopBoarding: 0,
          StopSequence: 26,
          StopPosition: {
            PositionLat: 24.18759,
            PositionLon: 120.702398
          },
          StationNameID: "4673",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13260",
          StopID: "13260",
          StopName: {
            Zh_tw: "中山中興路口",
            En: "Zhongshan-Zhongxing Intersection"
          },
          StopBoarding: 0,
          StopSequence: 27,
          StopPosition: {
            PositionLat: 24.191603,
            PositionLon: 120.702433
          },
          StationNameID: "4659",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13336",
          StopID: "13336",
          StopName: {
            Zh_tw: "頭家厝車站",
            En: "Touqiancuo Station"
          },
          StopBoarding: 0,
          StopSequence: 28,
          StopPosition: {
            PositionLat: 24.195397,
            PositionLon: 120.702435
          },
          StationNameID: "6461",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13672",
          StopID: "13672",
          StopName: {
            Zh_tw: "瓦窯(中山路)",
            En: "Wayao(Zhongshan Rd.)"
          },
          StopBoarding: 0,
          StopSequence: 29,
          StopPosition: {
            PositionLat: 24.199937,
            PositionLon: 120.703217
          },
          StationNameID: "6536",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13230",
          StopID: "13230",
          StopName: {
            Zh_tw: "僑忠國小",
            En: "Chyau-Zhong Elementary School"
          },
          StopBoarding: 0,
          StopSequence: 30,
          StopPosition: {
            PositionLat: 24.202855,
            PositionLon: 120.703897
          },
          StationNameID: "3567",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13095",
          StopID: "13095",
          StopName: {
            Zh_tw: "中山合作街口",
            En: "Zhongshan-Hecuo Intersection"
          },
          StopBoarding: 0,
          StopSequence: 31,
          StopPosition: {
            PositionLat: 24.204395,
            PositionLon: 120.704323
          },
          StationNameID: "4658",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13319",
          StopID: "13319",
          StopName: {
            Zh_tw: "中山圓通南路口",
            En: "Zhongshan-Yuantong S. Intersection"
          },
          StopBoarding: 0,
          StopSequence: 32,
          StopPosition: {
            PositionLat: 24.2076137443,
            PositionLon: 120.705231428
          },
          StationNameID: "4370",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13331",
          StopID: "13331",
          StopName: {
            Zh_tw: "中山潭子街口",
            En: "Zhongshan-Tanzi Intersection"
          },
          StopBoarding: 0,
          StopSequence: 33,
          StopPosition: {
            PositionLat: 24.209493,
            PositionLon: 120.70522
          },
          StationNameID: "6462",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13329",
          StopID: "13329",
          StopName: {
            Zh_tw: "潭子車站",
            En: "Tanzi Station"
          },
          StopBoarding: 0,
          StopSequence: 34,
          StopPosition: {
            PositionLat: 24.212598,
            PositionLon: 120.705423
          },
          StationNameID: "6473",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG1649",
          StopID: "1649",
          StopName: {
            Zh_tw: "潭子國小",
            En: "Tanzi Elementary School"
          },
          StopBoarding: 0,
          StopSequence: 35,
          StopPosition: {
            PositionLat: 24.21499252319336,
            PositionLon: 120.70509338378906
          },
          StationNameID: "6012",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG21259",
          StopID: "21259",
          StopName: {
            Zh_tw: "潭子加工區",
            En: "Taichung Export Processing Zone"
          },
          StopBoarding: 0,
          StopSequence: 36,
          StopPosition: {
            PositionLat: 24.216438,
            PositionLon: 120.705515
          },
          StationNameID: "3741",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13332",
          StopID: "13332",
          StopName: {
            Zh_tw: "潭秀里",
            En: "Tanxiu Village"
          },
          StopBoarding: 0,
          StopSequence: 37,
          StopPosition: {
            PositionLat: 24.221308,
            PositionLon: 120.706417
          },
          StationNameID: "3743",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13311",
          StopID: "13311",
          StopName: {
            Zh_tw: "矽品精密",
            En: "S.P.I.L."
          },
          StopBoarding: 0,
          StopSequence: 38,
          StopPosition: {
            PositionLat: 24.22424,
            PositionLon: 120.707305
          },
          StationNameID: "4361",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13300",
          StopID: "13300",
          StopName: {
            Zh_tw: "弘文中學",
            En: "Hongwen Junior High School"
          },
          StopBoarding: 0,
          StopSequence: 39,
          StopPosition: {
            PositionLat: 24.226553,
            PositionLon: 120.7077
          },
          StationNameID: "1909",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG19426",
          StopID: "19426",
          StopName: {
            Zh_tw: "中山祥和路口",
            En: "Zhongshan-Xianghe Intersection"
          },
          StopBoarding: 0,
          StopSequence: 40,
          StopPosition: {
            PositionLat: 24.228252,
            PositionLon: 120.708142
          },
          StationNameID: "0539",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13313",
          StopID: "13313",
          StopName: {
            Zh_tw: "校栗林",
            En: "Xiaolilin"
          },
          StopBoarding: 0,
          StopSequence: 41,
          StopPosition: {
            PositionLat: 24.231507,
            PositionLon: 120.708697
          },
          StationNameID: "2785",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13302",
          StopID: "13302",
          StopName: {
            Zh_tw: "栗林車站",
            En: "Lilin Station"
          },
          StopBoarding: 0,
          StopSequence: 42,
          StopPosition: {
            PositionLat: 24.235103,
            PositionLon: 120.709642
          },
          StationNameID: "6463",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13318",
          StopID: "13318",
          StopName: {
            Zh_tw: "菸廠",
            En: "Tobacco Factory"
          },
          StopBoarding: 0,
          StopSequence: 43,
          StopPosition: {
            PositionLat: 24.23688,
            PositionLon: 120.710303
          },
          StationNameID: "3282",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13264",
          StopID: "13264",
          StopName: {
            Zh_tw: "文化新村",
            En: "Cultural Community"
          },
          StopBoarding: 0,
          StopSequence: 44,
          StopPosition: {
            PositionLat: 24.238367,
            PositionLon: 120.710855
          },
          StationNameID: "1661",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13335",
          StopID: "13335",
          StopName: {
            Zh_tw: "輸配電",
            En: "Power Distribution"
          },
          StopBoarding: 0,
          StopSequence: 45,
          StopPosition: {
            PositionLat: 24.241535,
            PositionLon: 120.7127
          },
          StationNameID: "3817",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13345",
          StopID: "13345",
          StopName: {
            Zh_tw: "豐原分局",
            En: "Fengyuan Police Office"
          },
          StopBoarding: 0,
          StopSequence: 46,
          StopPosition: {
            PositionLat: 24.243548,
            PositionLon: 120.71377
          },
          StationNameID: "6210",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13339",
          StopID: "13339",
          StopName: {
            Zh_tw: "豐原高商",
            En: "Fengyuan Voc. School"
          },
          StopBoarding: 0,
          StopSequence: 47,
          StopPosition: {
            PositionLat: 24.247538,
            PositionLon: 120.715302
          },
          StationNameID: "3938",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13324",
          StopID: "13324",
          StopName: {
            Zh_tw: "電信局",
            En: "Telecom Company"
          },
          StopBoarding: 0,
          StopSequence: 48,
          StopPosition: {
            PositionLat: 24.250033,
            PositionLon: 120.714747
          },
          StationNameID: "3556",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13243",
          StopID: "13243",
          StopName: {
            Zh_tw: "臺灣企銀(豐原郵局)",
            En: "Taiwan Business Bank (Fengyuan Post Office)"
          },
          StopBoarding: 0,
          StopSequence: 49,
          StopPosition: {
            PositionLat: 24.251365,
            PositionLon: 120.715257
          },
          StationNameID: "6250",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13320",
          StopID: "13320",
          StopName: {
            Zh_tw: "媽祖廟",
            En: "Mazu Temple"
          },
          StopBoarding: 0,
          StopSequence: 50,
          StopPosition: {
            PositionLat: 24.251575,
            PositionLon: 120.718513
          },
          StationNameID: "3343",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13308",
          StopID: "13308",
          StopName: {
            Zh_tw: "和平街",
            En: "Heping St."
          },
          StopBoarding: 0,
          StopSequence: 51,
          StopPosition: {
            PositionLat: 24.25233,
            PositionLon: 120.719862
          },
          StationNameID: "2309",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG11367",
          StopID: "11367",
          StopName: {
            Zh_tw: "豐原",
            En: "Fengyuan"
          },
          StopBoarding: 0,
          StopSequence: 52,
          StopPosition: {
            PositionLat: 24.253709,
            PositionLon: 120.721193
          },
          StationNameID: "3935",
          LocationCityCode: "TXG"
        }
      ],
      UpdateTime: "2019-10-22T00:12:24+08:00",
      VersionID: 125
    },
    {
      Direction: 1,
      Stops: [
        {
          StopUID: "TXG6693",
          StopID: "6693",
          StopName: {
            Zh_tw: "豐原",
            En: "Fengyuan"
          },
          StopBoarding: 0,
          StopSequence: 1,
          StopPosition: {
            PositionLat: 24.25396,
            PositionLon: 120.721824
          },
          StationNameID: "3935",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13320",
          StopID: "13320",
          StopName: {
            Zh_tw: "媽祖廟",
            En: "Mazu Temple"
          },
          StopBoarding: 0,
          StopSequence: 2,
          StopPosition: {
            PositionLat: 24.251575,
            PositionLon: 120.718513
          },
          StationNameID: "3343",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13244",
          StopID: "13244",
          StopName: {
            Zh_tw: "臺灣企銀(豐原郵局)",
            En: "Taiwan Business Bank (Fengyuan Post Office)"
          },
          StopBoarding: 0,
          StopSequence: 3,
          StopPosition: {
            PositionLat: 24.251405,
            PositionLon: 120.715518
          },
          StationNameID: "6250",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13324",
          StopID: "13324",
          StopName: {
            Zh_tw: "電信局",
            En: "Telecom Company"
          },
          StopBoarding: 0,
          StopSequence: 4,
          StopPosition: {
            PositionLat: 24.250033,
            PositionLon: 120.714747
          },
          StationNameID: "3556",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13339",
          StopID: "13339",
          StopName: {
            Zh_tw: "豐原高商",
            En: "Fengyuan Voc. School"
          },
          StopBoarding: 0,
          StopSequence: 5,
          StopPosition: {
            PositionLat: 24.247538,
            PositionLon: 120.715302
          },
          StationNameID: "3938",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13345",
          StopID: "13345",
          StopName: {
            Zh_tw: "豐原分局",
            En: "Fengyuan Police Office"
          },
          StopBoarding: 0,
          StopSequence: 6,
          StopPosition: {
            PositionLat: 24.243548,
            PositionLon: 120.71377
          },
          StationNameID: "6210",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13335",
          StopID: "13335",
          StopName: {
            Zh_tw: "輸配電",
            En: "Power Distribution"
          },
          StopBoarding: 0,
          StopSequence: 7,
          StopPosition: {
            PositionLat: 24.241535,
            PositionLon: 120.7127
          },
          StationNameID: "3817",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13264",
          StopID: "13264",
          StopName: {
            Zh_tw: "文化新村",
            En: "Cultural Community"
          },
          StopBoarding: 0,
          StopSequence: 8,
          StopPosition: {
            PositionLat: 24.238367,
            PositionLon: 120.710855
          },
          StationNameID: "1661",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13318",
          StopID: "13318",
          StopName: {
            Zh_tw: "菸廠",
            En: "Tobacco Factory"
          },
          StopBoarding: 0,
          StopSequence: 9,
          StopPosition: {
            PositionLat: 24.23688,
            PositionLon: 120.710303
          },
          StationNameID: "3282",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13302",
          StopID: "13302",
          StopName: {
            Zh_tw: "栗林車站",
            En: "Lilin Station"
          },
          StopBoarding: 0,
          StopSequence: 10,
          StopPosition: {
            PositionLat: 24.235103,
            PositionLon: 120.709642
          },
          StationNameID: "6463",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13313",
          StopID: "13313",
          StopName: {
            Zh_tw: "校栗林",
            En: "Xiaolilin"
          },
          StopBoarding: 0,
          StopSequence: 11,
          StopPosition: {
            PositionLat: 24.231507,
            PositionLon: 120.708697
          },
          StationNameID: "2785",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG19426",
          StopID: "19426",
          StopName: {
            Zh_tw: "中山祥和路口",
            En: "Zhongshan-Xianghe Intersection"
          },
          StopBoarding: 0,
          StopSequence: 12,
          StopPosition: {
            PositionLat: 24.228252,
            PositionLon: 120.708142
          },
          StationNameID: "0539",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13300",
          StopID: "13300",
          StopName: {
            Zh_tw: "弘文中學",
            En: "Hongwen Junior High School"
          },
          StopBoarding: 0,
          StopSequence: 13,
          StopPosition: {
            PositionLat: 24.226553,
            PositionLon: 120.7077
          },
          StationNameID: "1909",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13311",
          StopID: "13311",
          StopName: {
            Zh_tw: "矽品精密",
            En: "S.P.I.L."
          },
          StopBoarding: 0,
          StopSequence: 14,
          StopPosition: {
            PositionLat: 24.22424,
            PositionLon: 120.707305
          },
          StationNameID: "4361",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13332",
          StopID: "13332",
          StopName: {
            Zh_tw: "潭秀里",
            En: "Tanxiu Village"
          },
          StopBoarding: 0,
          StopSequence: 15,
          StopPosition: {
            PositionLat: 24.221308,
            PositionLon: 120.706417
          },
          StationNameID: "3743",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13330",
          StopID: "13330",
          StopName: {
            Zh_tw: "潭子加工區",
            En: "Taichung Export Processing Zone"
          },
          StopBoarding: 0,
          StopSequence: 16,
          StopPosition: {
            PositionLat: 24.217975,
            PositionLon: 120.70569
          },
          StationNameID: "3741",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG1649",
          StopID: "1649",
          StopName: {
            Zh_tw: "潭子國小",
            En: "Tanzi Elementary School"
          },
          StopBoarding: 0,
          StopSequence: 17,
          StopPosition: {
            PositionLat: 24.21499252319336,
            PositionLon: 120.70509338378906
          },
          StationNameID: "6012",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13329",
          StopID: "13329",
          StopName: {
            Zh_tw: "潭子車站",
            En: "Tanzi Station"
          },
          StopBoarding: 0,
          StopSequence: 18,
          StopPosition: {
            PositionLat: 24.212598,
            PositionLon: 120.705423
          },
          StationNameID: "6473",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13331",
          StopID: "13331",
          StopName: {
            Zh_tw: "中山潭子街口",
            En: "Zhongshan-Tanzi Intersection"
          },
          StopBoarding: 0,
          StopSequence: 19,
          StopPosition: {
            PositionLat: 24.209493,
            PositionLon: 120.70522
          },
          StationNameID: "6462",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13319",
          StopID: "13319",
          StopName: {
            Zh_tw: "中山圓通南路口",
            En: "Zhongshan-Yuantong S. Intersection"
          },
          StopBoarding: 0,
          StopSequence: 20,
          StopPosition: {
            PositionLat: 24.2076137443,
            PositionLon: 120.705231428
          },
          StationNameID: "4370",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13096",
          StopID: "13096",
          StopName: {
            Zh_tw: "中山合作街口",
            En: "Zhongshan-Hecuo Intersection"
          },
          StopBoarding: 0,
          StopSequence: 21,
          StopPosition: {
            PositionLat: 24.204858,
            PositionLon: 120.704412
          },
          StationNameID: "4658",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13229",
          StopID: "13229",
          StopName: {
            Zh_tw: "僑忠國小",
            En: "Chyau-Zhong Elementary School"
          },
          StopBoarding: 0,
          StopSequence: 22,
          StopPosition: {
            PositionLat: 24.202103,
            PositionLon: 120.703698
          },
          StationNameID: "3567",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13672",
          StopID: "13672",
          StopName: {
            Zh_tw: "瓦窯(中山路)",
            En: "Wayao(Zhongshan Rd.)"
          },
          StopBoarding: 0,
          StopSequence: 23,
          StopPosition: {
            PositionLat: 24.199937,
            PositionLon: 120.703217
          },
          StationNameID: "6536",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13336",
          StopID: "13336",
          StopName: {
            Zh_tw: "頭家厝車站",
            En: "Touqiancuo Station"
          },
          StopBoarding: 0,
          StopSequence: 24,
          StopPosition: {
            PositionLat: 24.195397,
            PositionLon: 120.702435
          },
          StationNameID: "6461",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13260",
          StopID: "13260",
          StopName: {
            Zh_tw: "中山中興路口",
            En: "Zhongshan-Zhongxing Intersection"
          },
          StopBoarding: 0,
          StopSequence: 25,
          StopPosition: {
            PositionLat: 24.191603,
            PositionLon: 120.702433
          },
          StationNameID: "4659",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13325",
          StopID: "13325",
          StopName: {
            Zh_tw: "中山路一巷口",
            En: "Zhongshan Rd. 1st. Ln. Intersection"
          },
          StopBoarding: 0,
          StopSequence: 26,
          StopPosition: {
            PositionLat: 24.18759,
            PositionLon: 120.702398
          },
          StationNameID: "4673",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG2257",
          StopID: "2257",
          StopName: {
            Zh_tw: "捷運松竹站(北屯路)",
            En: "MRT Songzhu Station(Beitun Rd.)"
          },
          StopBoarding: 0,
          StopSequence: 27,
          StopPosition: {
            PositionLat: 24.181584,
            PositionLon: 120.701638
          },
          StationNameID: "6464",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13286",
          StopID: "13286",
          StopName: {
            Zh_tw: "北新國中",
            En: "Beixin Junior High School"
          },
          StopBoarding: 0,
          StopSequence: 28,
          StopPosition: {
            PositionLat: 24.17842,
            PositionLon: 120.700337
          },
          StationNameID: "0105",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13299",
          StopID: "13299",
          StopName: {
            Zh_tw: "北屯崇德二路口",
            En: "Beitun-Chongde 2nd Intersection"
          },
          StopBoarding: 0,
          StopSequence: 29,
          StopPosition: {
            PositionLat: 24.175848,
            PositionLon: 120.699317
          },
          StationNameID: "0200",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13314",
          StopID: "13314",
          StopName: {
            Zh_tw: "特力屋北屯店",
            En: "B&Q Beitun Branch"
          },
          StopBoarding: 0,
          StopSequence: 30,
          StopPosition: {
            PositionLat: 24.173743,
            PositionLon: 120.698344
          },
          StationNameID: "0364",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG17947",
          StopID: "17947",
          StopName: {
            Zh_tw: "北屯文心路口",
            En: "Beitun-Wenxin Rd. Intersection"
          },
          StopBoarding: 0,
          StopSequence: 31,
          StopPosition: {
            PositionLat: 24.17061,
            PositionLon: 120.697915
          },
          StationNameID: "4951",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13284",
          StopID: "13284",
          StopName: {
            Zh_tw: "大坑口",
            En: "Dakengkou"
          },
          StopBoarding: 0,
          StopSequence: 32,
          StopPosition: {
            PositionLat: 24.169732,
            PositionLon: 120.697165
          },
          StationNameID: "0103",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13259",
          StopID: "13259",
          StopName: {
            Zh_tw: "三光國中",
            En: "Sanguang junior high school"
          },
          StopBoarding: 0,
          StopSequence: 33,
          StopPosition: {
            PositionLat: 24.167619,
            PositionLon: 120.695909
          },
          StationNameID: "5511",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13283",
          StopID: "13283",
          StopName: {
            Zh_tw: "北屯",
            En: "Beitun"
          },
          StopBoarding: 0,
          StopSequence: 34,
          StopPosition: {
            PositionLat: 24.165043,
            PositionLon: 120.694182
          },
          StationNameID: "0492",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13346",
          StopID: "13346",
          StopName: {
            Zh_tw: "北屯國小(北屯路)",
            En: "Beitun Elementary School(Beitun Rd.)"
          },
          StopBoarding: 0,
          StopSequence: 35,
          StopPosition: {
            PositionLat: 24.16325,
            PositionLon: 120.69318
          },
          StationNameID: "5405",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13326",
          StopID: "13326",
          StopName: {
            Zh_tw: "監理站",
            En: "Motor Vehicles Office"
          },
          StopBoarding: 0,
          StopSequence: 36,
          StopPosition: {
            PositionLat: 24.161057,
            PositionLon: 120.69209
          },
          StationNameID: "0892",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13342",
          StopID: "13342",
          StopName: {
            Zh_tw: "寶覺寺",
            En: "Baojue Temple"
          },
          StopBoarding: 0,
          StopSequence: 37,
          StopPosition: {
            PositionLat: 24.158027,
            PositionLon: 120.689922
          },
          StationNameID: "0960",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13322",
          StopID: "13322",
          StopName: {
            Zh_tw: "新民高中(三民路)",
            En: "Shin-min Senior High School(Sanmin Rd.)"
          },
          StopBoarding: 0,
          StopSequence: 38,
          StopPosition: {
            PositionLat: 24.156805,
            PositionLon: 120.688503
          },
          StationNameID: "4399",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG1531",
          StopID: "1531",
          StopName: {
            Zh_tw: "三民錦中街口",
            En: "Sanmin-Jinzhong Intersection"
          },
          StopBoarding: 0,
          StopSequence: 39,
          StopPosition: {
            PositionLat: 24.1555633333333,
            PositionLon: 120.687098333333
          },
          StationNameID: "0934",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13251",
          StopID: "13251",
          StopName: {
            Zh_tw: "一心市場",
            En: "Yixin Market"
          },
          StopBoarding: 0,
          StopSequence: 40,
          StopPosition: {
            PositionLat: 24.153663,
            PositionLon: 120.685713
          },
          StationNameID: "0047",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG2249",
          StopID: "2249",
          StopName: {
            Zh_tw: "中友百貨",
            En: "Chungyo Department Store"
          },
          StopBoarding: 0,
          StopSequence: 41,
          StopPosition: {
            PositionLat: 24.151767,
            PositionLon: 120.684835
          },
          StationNameID: "0046",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13293",
          StopID: "13293",
          StopName: {
            Zh_tw: "國立臺中科技大學",
            En: "National Taichung University of Science and Technology"
          },
          StopBoarding: 0,
          StopSequence: 42,
          StopPosition: {
            PositionLat: 24.149867,
            PositionLon: 120.68413
          },
          StationNameID: "0045",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG16296",
          StopID: "16296",
          StopName: {
            Zh_tw: "中興堂",
            En: "Chunghsing Hall"
          },
          StopBoarding: 0,
          StopSequence: 43,
          StopPosition: {
            PositionLat: 24.146209,
            PositionLon: 120.684631
          },
          StationNameID: "1513",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13289",
          StopID: "13289",
          StopName: {
            Zh_tw: "臺中公園(雙十路)",
            En: "Taichung Park (Shuangshi Rd.)"
          },
          StopBoarding: 0,
          StopSequence: 44,
          StopPosition: {
            PositionLat: 24.1439927651,
            PositionLon: 120.686123371
          },
          StationNameID: "4544",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13253",
          StopID: "13253",
          StopName: {
            Zh_tw: "干城站",
            En: "Gancheng Station"
          },
          StopBoarding: 0,
          StopSequence: 45,
          StopPosition: {
            PositionLat: 24.140888,
            PositionLon: 120.685985
          },
          StationNameID: "0402",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG7351",
          StopID: "7351",
          StopName: {
            Zh_tw: "臺中車站(民族路口)",
            En: "Taichung Station(Minzu Rd. Intersection)"
          },
          StopBoarding: 0,
          StopSequence: 46,
          StopPosition: {
            PositionLat: 24.136224,
            PositionLon: 120.682876
          },
          StationNameID: "6510",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13344",
          StopID: "13344",
          StopName: {
            Zh_tw: "民權繼光街口",
            En: "Minquan-Jiguang Intersection"
          },
          StopBoarding: 0,
          StopSequence: 47,
          StopPosition: {
            PositionLat: 24.136985,
            PositionLon: 120.681122
          },
          StationNameID: "4284",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13287",
          StopID: "13287",
          StopName: {
            Zh_tw: "臺中女中",
            En: "Taichung Girls Senior High School"
          },
          StopBoarding: 0,
          StopSequence: 48,
          StopPosition: {
            PositionLat: 24.135705,
            PositionLon: 120.677847
          },
          StationNameID: "0071",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG13305",
          StopID: "13305",
          StopName: {
            Zh_tw: "地方法院",
            En: "Taichung District Court"
          },
          StopBoarding: 0,
          StopSequence: 49,
          StopPosition: {
            PositionLat: 24.133875,
            PositionLon: 120.675773
          },
          StationNameID: "0070",
          LocationCityCode: "TXG"
        },
        {
          StopUID: "TXG10005",
          StopID: "10005",
          StopName: {
            Zh_tw: "光明國中(貴和街)",
            En: "Guang Ming Junior High School(Guei Han Street)"
          },
          StopBoarding: 0,
          StopSequence: 50,
          StopPosition: {
            PositionLat: 24.133201,
            PositionLon: 120.674334
          },
          StationNameID: "4091",
          LocationCityCode: "TXG"
        }
      ],
      UpdateTime: "2019-10-22T00:12:24+08:00",
      VersionID: 125
    }
  ]);
  Mock.mock(new RegExp('v2/Bus/Route/City/Taichung/55.*'), [
    {
      HasSubRoutes: true,
      BusRouteType: 11,
      DepartureStopNameZh: "地方法院",
      DestinationStopNameZh: "豐原",
      UpdateTime: "2019-10-22T00:12:24+08:00",
      VersionID: 125
    }
  ]);
  Mock.mock(new RegExp('v2/Bus/Shape/City/Taichung/55.*'), [
    {
      RouteUID: "TXG55",
      RouteID: "55",
      RouteName: {
        Zh_tw: "55",
        En: "55"
      },
      Direction: 0,
      Geometry:
        "MULTILINESTRING((120.712880000312 24.2417999997701,120.712989999989 24.2417300001394,120.713110000127 24.2419500003924,120.714079999892 24.2438800003617,120.714389999799 24.2446299998746,120.714540000421 24.245039999896,120.715169999796 24.2475699996559,120.715340000441 24.2482300004142,120.714739999751 24.2500299997847,120.714429999845 24.2509800004267,120.715300000395 24.2512500002873,120.716620000113 24.2517900000086,120.71760000034 24.2518599996392,120.718539999621 24.2517099999166,120.718830000404 24.2516600003089,120.719940000331 24.2517000003549,120.71992999987 24.2523299997297,120.719920000308 24.2525799995673,120.720239999776 24.2526199996133,120.720370000375 24.2527100001665,120.720839999566 24.2536700003704,120.7218700003 24.2538899997236),(120.707739999801 24.2265600002438,120.707839999916 24.226540000221,120.708100000215 24.2274600003788,120.708519999798 24.229339999841,120.708920000258 24.2323100001064,120.709139999611 24.2331500001726,120.709350000302 24.2339100001464,120.710480000252 24.2370300001344,120.711089999604 24.2386799997823,120.711369999926 24.2392900000334,120.712989999989 24.2417300001394),(120.705700000155 24.2180099998615,120.705809999832 24.2179899998388,120.706249000291 24.219705999832,120.706489999714 24.2207300002893,120.707300000195 24.224240000276,120.707839999916 24.226540000221),(120.705290000133 24.2107299995898,120.705439999856 24.210720000028,120.705459999879 24.2115800001169,120.705390000248 24.2126000003898,120.705219999603 24.2149999995505,120.705219999603 24.2150599996193,120.705259999649 24.2156699998707,120.705809999832 24.2179899998388),(120.67412850023 24.1333209102319,120.67466499979 24.1329488499096,120.677970000215 24.1360100000614,120.679920000208 24.1378799999621,120.680740000251 24.137180000057,120.682289999784 24.1357899998086,120.682619999713 24.1359999996002,120.68419999973 24.1367000004047,120.684410000421 24.1371100004263,120.684649999798 24.1374200003327,120.684820000443 24.1376599997093,120.685139999911 24.1377999998702,120.685659999609 24.1383700000755,120.686020000023 24.1388699997508,120.686020000023 24.1395699996559,120.685970000415 24.1398600004386,120.685970000415 24.1400599997692,120.686 24.140280000022,120.685990000438 24.1408900002732,120.685930000369 24.1434499996177,120.686499999675 24.1451699997957,120.686510000137 24.1454199996334,120.686430000044 24.1457800000471,120.686249999838 24.1460800003918,120.686009999562 24.1461799996073,120.684410000421 24.1462500001374,120.684540000121 24.1462399996763,120.684099999615 24.1462500001376,120.683720000078 24.1461500000225,120.683098000173 24.145911999839,120.682476000267 24.1459210002541,120.684130000099 24.1498699998006,120.684090000054 24.1498800002619,120.685210000441 24.1524999996754,120.685710000117 24.1536600001089,120.686169999746 24.1546899999434,120.686380000437 24.1548100000814,120.689699999755 24.157640000186,120.690980000327 24.1588199997432,120.692230000414 24.1614400000559,120.692649999998 24.1622899996838,120.693180000157 24.1632499998876,120.694219999553 24.1650199996733,120.695879999662 24.1676300004243,120.697220000303 24.1696999996554,120.698089999953 24.1710499998575,120.698259999699 24.171499999925,120.698310000207 24.1718099998318,120.698290000183 24.173240000126,120.698339999791 24.1736900001934,120.698459999929 24.1740499997077,120.698479999952 24.1740899997537,120.699290000433 24.1758600004387,120.700420000383 24.1783900001984,120.701740000101 24.1813500000027,120.701960000354 24.1821900000684,120.702059999569 24.1829199995585,120.702509999637 24.1861900001684,120.702509999637 24.1875899999785,120.702489999614 24.1915999996404,120.702480000052 24.1944800002518,120.702520000098 24.1953899999487,120.702669999821 24.1968200002429,120.703210000441 24.1994100000715,120.70360000044 24.2011399998112,120.704049999608 24.202819999943,120.704459999629 24.204359999914,120.705120000388 24.2067399999511,120.705259999649 24.2078400003159,120.705330000179 24.2089100001963,120.705439999856 24.210720000028))",
      UpdateTime: "2019-10-22T00:12:24+08:00",
      VersionID: 125
    },
    {
      RouteUID: "TXG55",
      RouteID: "55",
      RouteName: {
        Zh_tw: "55",
        En: "55"
      },
      Direction: 1,
      Geometry:
        "LINESTRING(120.721935999747 24.2539099997467,120.718738999805 24.2533619996566,120.718759999874 24.2516990003087,120.717967000177 24.2518560003542,120.716658000067 24.2518560003542,120.715671000416 24.2514250002636,120.71509099975 24.2511710002415,120.714446999729 24.2510730002188,120.715305999772 24.2482169998148,120.714468999844 24.2451060002418,120.712966999827 24.2418779997699,120.711143000249 24.2389820002192,120.708889999774 24.2325250001287,120.708525000029 24.230411999814,120.707859999939 24.2268900001734,120.707066000196 24.2233869996104,120.705713999901 24.2176339996095,120.705241999719 24.2148160000584,120.705456999741 24.2111560003492,120.705178000365 24.2072809997184,120.704277000183 24.2038170000546,120.702560000144 24.1963599997143,120.702452999706 24.1917019998475,120.702495999891 24.1867099998667,120.701872999939 24.1817189999319,120.699159999834 24.1755699996558,120.698459999929 24.1740499997078,120.698339999791 24.1736900001934,120.698279999722 24.1730100003113,120.698310000206 24.1718099998317,120.698259999699 24.1714999999251,120.698089999954 24.1710499998576,120.69780000007 24.1705500001824,120.696950000442 24.1692899996338,120.694169999946 24.1649399995814,120.693100000065 24.1631099997268,120.692649999998 24.1622899996838,120.691294000418 24.1592139999262,120.689539999571 24.1576699997707,120.6879999996 24.1563599996143,120.687239999626 24.1557199997782,120.686198000138 24.1547320000818,120.682454000152 24.1459020002771,120.683216000218 24.1459509998388,120.684117000399 24.1462740003449,120.685446999679 24.1462049998609,120.686037999954 24.1461760003222,120.686320000368 24.1456100003013,120.68632999993 24.1453799995874,120.685959999954 24.1441899995689,120.685730000139 24.14340000001,120.685770000185 24.1418499995779,120.685791000255 24.1402719996531,120.685979999977 24.1397200002779,120.686020000023 24.1395699996558,120.686037999954 24.139195000349,120.686020000023 24.1388699997507,120.685659999609 24.1383700000755,120.685389999749 24.1381000002149,120.685139999911 24.1377999998701,120.684660000259 24.1375900000785,120.684370000375 24.1373299997797,120.684210000191 24.1368799997123,120.684059999569 24.1367200004277,120.682209999692 24.1358899999236,120.681019999673 24.1369700002654,120.679960000254 24.137920000008,120.677709999917 24.1357699997857,120.674686400057 24.1328313597795,120.67412850023 24.1332230001414)",
      UpdateTime: "2019-10-22T00:12:24+08:00",
      VersionID: 125
    }
  ]);
  Mock.mock(new RegExp('v2/Bus/RealTimeByFrequency/City/Taichung/55.*'), [
    {
      PlateNumb: "016-FV",
      Direction: 0,
      BusPosition: {
        PositionLat: 24.19215,
        PositionLon: 120.702439
      },
      Speed: 33,
      Azimuth: 1,
      DutyStatus: 0,
      BusStatus: 0,
      MessageType: 0,
      GPSTime: "2019-10-22T07:58:19+08:00",
      SrcUpdateTime: "2019-10-22T07:58:25+08:00",
      UpdateTime: "2019-10-22T08:00:19+08:00"
    },
    {
      PlateNumb: "709-FX",
      Direction: 0,
      BusPosition: {
        PositionLat: 24.20813,
        PositionLon: 120.7052
      },
      Speed: 21,
      Azimuth: 1,
      DutyStatus: 0,
      BusStatus: 0,
      MessageType: 0,
      GPSTime: "2019-10-22T07:58:14+08:00",
      SrcUpdateTime: "2019-10-22T07:58:25+08:00",
      UpdateTime: "2019-10-22T08:00:19+08:00"
    },
    {
      PlateNumb: "FAE-757",
      Direction: 1,
      BusPosition: {
        PositionLat: 24.169243,
        PositionLon: 120.696853
      },
      Speed: 0,
      Azimuth: 0,
      DutyStatus: 0,
      BusStatus: 0,
      MessageType: 0,
      GPSTime: "2019-10-22T07:58:17+08:00",
      SrcUpdateTime: "2019-10-22T07:58:25+08:00",
      UpdateTime: "2019-10-22T08:00:19+08:00"
    }
  ]);
}
