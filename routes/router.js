const express = require("express");

const { compute, computeMortgage } = require("../components/functions");

const router = express.Router();

router.get("/", (req, res) => {
    try {
        const resources = computeMortgage();
        res.status(200).json(resources);
    } catch (error) {
        res.status(500).json({ message: 'Error retrieving resources' });
    }
});

module.exports = router;
