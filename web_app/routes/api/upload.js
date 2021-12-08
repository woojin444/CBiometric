const express = require("express");
const fs = require("fs");
const path = require("path");
const router = express.Router();
const shortid = require("shortid");

// @route   GET api/upload/test
// @desc    Test upload route
// @route   Public
router.get("/test", (req, res) => res.json({ msg: "upload Works" }));

router.post("/image", (req, res) => {
  let imageFile = req.files.file;
  const recog_path =
    __dirname.substring(0, __dirname.indexOf("web_app")) +
    "facenet-master/src/";
  const file_path = recog_path + "data/initial_image/abc/";

  fs.readdir(file_path, (err, files) => {
    if (err) {
      console.log(err);
      // return res.status(500).send(err);
    } else {
      for (const file of files) {
        fs.unlink(path.join(file_path, file), err => {
          if (err) {
            console.log(err);
            // return res.status(501).send(err);
          }
        });
      }
      imageFile.mv(file_path + req.body.filename, function(err, results) {
        if (err) {
          console.log(err);
          // return res.status(500).send(err);
        } else {
          const reportID = shortid.generate(file_path + req.body.filename);
          const resize =
            "python " +
            recog_path +
            "align/align_dataset_mtcnn.py " +
            recog_path +
            "data/initial_image/ --image_size 160 --margin 32 --random_order --gpu_memory_fraction 0.25 " +
            recog_path +
            "data/target/" +
            reportID +
            "/ --detect_multiple_faces true";

          const search = "python " + recog_path + "search.py " + reportID;

          const report =
            "python " + recog_path + "generateReport.py " + reportID;

          console.log(reportID);
          res.json(reportID);

          var exec = require("child_process").exec;
          exec(resize, function(err, stdout, stderr) {
            if (err) {
              console.log("error ", stderr);
              // return res.status(501).send(err);
            } else {
              console.log("resize done. \n" + stdout);
              exec(search, function(err, stdout, stderr) {
                // if (err) {
                //   console.log("error ", stderr);
                //   // return res.status(502).send(err);
                // } else {
                  console.log("search done", stdout);
                  exec(report, function(err, stdout, stderr) {
                    if (err) {
                      console.log("error ", stderr);
                      // return res.status(503).send(err);
                    } else {
                      console.log("Report generated");
                      // res.json({ status: true });
                    }
                  });
                // }
              });
            }
          });
        }
      });
    }
  });

  //
});

module.exports = router;
