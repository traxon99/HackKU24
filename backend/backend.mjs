import { MongoClient } from 'mongodb';

async function main() {
    const uri = "mongodb+srv://jcyanek:10192871Jy_@hackku.p8yernm.mongodb.net/?retryWrites=true&w=majority&appName=HackKU";
    const client = new MongoClient(uri);

    try {
        await client.connect();

        // Selecting a specific database
        const databaseName = "hackku";
        const database = client.db(databaseName);

        // Selecting a specific collection within the database
        const collectionName = "users";
        const collection = database.collection(collectionName);

        // Now you can perform operations on the 'collection'

        // For example, to find all documents in the collection:
        const documents = await collection.find().toArray();
        console.log(documents);

    } catch (e) {
        console.error(e);
    } finally {
        await client.close();
    }
}

main();
