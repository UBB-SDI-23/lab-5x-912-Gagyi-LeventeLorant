import { useState } from "react"
import { Film } from "../../models/Film";

export const FilmsShowAll = () => {
    const [films, setFilms] = useState([]);

    fetch("https://app.swaggerhub.com/apis/GAGYILORANT/movie-and_facts/1.0.0#/films/films_retrieve")
    .then((res) => res.json())
    .then((data) => setFilms(data));
  
    return (
      <div className="App">
        <h1>Films list</h1>
        <table>
            <tr>
                <th>#</th>
                <th>Film name</th>
                <th>Profit</th>
                <th>Rating</th>
            </tr>
            {films.map((film : Film, index) => (
                <tr>
                    <td>{index}</td>
                    <td>{film.name}</td>
                    <td>{film.profit}</td>
                    <td>{film.rating}</td>
                </tr>
            ))
            }
        </table>
      </div>
    )
  }
  