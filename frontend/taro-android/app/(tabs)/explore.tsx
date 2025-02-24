import React, { useEffect, useState } from "react";
import { View, Text, FlatList } from "react-native";
import getGames from "../services/api";

export default function GamesScreen() {
    const [games, setGames] = useState<{ results: { id: number; name: string }[] } | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        getGames()
            .then(data => {
                setGames(data);
                setLoading(false);
            })
            .catch(err => {
                setError('Error fetching games');
                setLoading(false);
            });
    }, []);

    if (loading) {
        return (
            <View>
                <Text>Loading...</Text>
            </View>
        );
    }

    if (error) {
        return (
            <View>
                <Text>{error}</Text>
            </View>
        );
    }

    return (
        <View>
            <Text>Explore</Text>
            {games ? (
                <FlatList
                    data={games.results}
                    renderItem={({ item }) => <Text key={item.id}>{item.name}</Text>}
                />
            ) : (
                <Text>No games found.</Text>
            )}
        </View>
    );
}