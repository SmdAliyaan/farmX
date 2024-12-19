const User = require('../models/userModel');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

// Registration
exports.register = async (req, res) => {
    const { name, email, password } = req.body;
    try {
        const userExist = await User.findOne({ email });
        if (userExist) return res.status(400).send('Email already exists');

        const user = new User({ name, email, password });
        await user.save();
        res.send('User registered successfully');
    } catch (err) {
        res.status(400).send(err);
    }
};

// Login
exports.login = async (req, res) => {
    const { email, password } = req.body;
    try {
        const user = await User.findOne({ email });
        if (!user) return res.status(400).send('Email or password is wrong');

        const validPass = await bcrypt.compare(password, user.password);
        if (!validPass) return res.status(400).send('Email or password is wrong');

        const token = jwt.sign({ _id: user._id }, process.env.TOKEN_SECRET);
        res.header('auth-token', token).send({ token });
    } catch (err) {
        res.status(400).send(err);
    }
};
