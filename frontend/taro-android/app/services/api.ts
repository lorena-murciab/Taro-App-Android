import axios from "axios";

const API_URL = "http://192.168.18.8:8000";  // Asegúrate de usar "http://"

export async function getGames() {
    try {
        const response = await axios.get(`${API_URL}/games`);
        console.log('Fetched games:', response.data);
        return response.data;
    } catch (error) {
        console.error('Error fetching games:', error);
        throw error;
    }
}

export default getGames;