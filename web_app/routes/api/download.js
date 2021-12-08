const express = require("express");
const fs = require("fs");
const router = express.Router();

// @route   GET api/download/test
// @desc    Test download route
// @route   Public
router.get("/test", (req, res) => res.json({ msg: "download Works" }));

router.post("/report", (req, res) => {
  const report_path =
    __dirname.substring(0, __dirname.indexOf("web_app")) +
    "/web_app/client/public/report/";
  const file = report_path + req.body.reportID + ".pdf";
  if (fs.existsSync(file)) {
    res.send("http://localhost:3000/report/" + req.body.reportID + ".pdf");
  } else {
    return res.status(600).send("error");
  }
});

module.exports = router;
