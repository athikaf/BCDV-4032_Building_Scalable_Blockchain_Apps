const express = require("express");
const fs = require("fs");
const path = require("path");

const vardir = path.resolve("/var");

const myfile = path.join(vardir, "vol.txt");
const router = express.Router();

const logic = require("../../ethereum/logic");

router.get("/", async (req, res, next) => {
  let message = await logic.getMessage();
  res.send(message);
});

router.get("/1", async (req, res, next) => {
  fs.writeFileSync(myfile, "test-data", "utf-8");
  res.send("working");
});

router.post("/", async (req, res, next) => {
  let message = await logic.setMessage(req.body.message);
  fs.writeFileSync(myfile, req.body.message, "utf-8");
  res.send(message.transactionHash);
});

module.exports = router;
