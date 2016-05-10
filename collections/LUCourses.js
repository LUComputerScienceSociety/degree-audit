LUCourses = new Mongo.Collection('luCourses');

LUCourses.allow({
    insert: function(userId, doc){
        return !!userId;
    },
    update: function(userId, doc){
        return !!userId;
    },
    remove: function(userId, doc){
        return !!userId;
    }
});

LUCoursesSchema = new SimpleSchema({
  Department_Code:{
    type: String,
    label:"Department Code"
  },
  Course_Number:{
    type: Number,
    label:"Course Number"
  },
  Course_Name:{
    type: String,
    label:"Course Name"
  },
  Course_Credits:{
    type: Number,
    label:"Course Credit"
  },
  Course_Description:{
    type: String,
    label:"Course description",
  }
});

LUCourses.attachSchema(LUCoursesSchema);
