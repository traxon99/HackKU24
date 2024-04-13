const express = require('express');
const mongoose = require('mongoose');

// Initialize Express app
const app = express();

// Middleware
app.use(express.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/myDatabase', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));
db.once('open', () => {
    console.log('Connected to MongoDB');
});

// Define a Mongoose schema
const Schema = mongoose.Schema;
const exampleSchema = new Schema({
    name: String,
    age: Number,
});

// Define a Mongoose model
const ExampleModel = mongoose.model('Example', exampleSchema);

// Example route - create a new document
app.post('/examples', async (req, res) => {
    try {
        const { name, age } = req.body;
        const example = new ExampleModel({ name, age });
        await example.save();
        res.status(201).json(example);
    } catch (err) {
        res.status(400).json({ message: err.message });
    }
});

// Example route - get all documents
app.get('/examples', async (req, res) => {
    try {
        const examples = await ExampleModel.find();
        res.json(examples);
    } catch (err) {
        res.status(500).json({ message: err.message });
    }
});

// Set up the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is listening on port ${PORT}`);
});
