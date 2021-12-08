const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");
const fileUpload = require("express-fileupload");
const cors = require("cors");

const users = require("./routes/api/users");
const upload = require("./routes/api/upload");
const download = require("./routes/api/download");

const app = express();
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(fileUpload());

// DB Config
const db = require("./config/keys").mongoURI;

//Connect to DB
mongoose
  .connect(
    db,
    { useNewUrlParser: true }
  )
  .then(() => console.log("MongoDB Connected"))
  .catch(err => console.log(err));

app.get("/", (req, res) => res.send("Hello World"));

// Use Routes
app.use("/api/users", users);
app.use("/api/upload", upload);
app.use("/api/download", download);

const port = process.env.PORT || 5000;

app.listen(port, () => console.log("Server running on port " + port));
