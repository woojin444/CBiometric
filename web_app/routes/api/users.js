const express = require("express");
const router = express.Router();


// @route   GET api/users/test
// @desc    Test users route
// @route   Public
router.get("/test", (req, res) => res.json({ msg: "Users Works" }));

module.exports = router;
