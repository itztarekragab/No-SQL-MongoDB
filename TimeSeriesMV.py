from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.timeseriesdemo

db.weather.aggregate([
  {
     $project: {
        date: {
           $dateToParts: { date: "$timestamp" }
        },
        temp: 1
     }
  },
  {
     $group: {
        _id: {
           date: {
              year: "$date.year",
              month: "$date.month",
              day: "$date.day"
           }
        },
        avgTmp: { $avg: "$temp" }
     }
  }, {
     $merge: { into: "dailytemperatureaverages", whenMatched: "replace" }
  }
])