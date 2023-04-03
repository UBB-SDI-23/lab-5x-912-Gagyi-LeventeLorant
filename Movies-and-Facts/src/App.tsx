
import { useState } from "react";
import CssBaseline from "@mui/material/CssBaseline";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import * as React from "react";
import { AppBar, Toolbar, IconButton, Typography, Button } from "@mui/material";
import MenuIcon from "@mui/icons-material/Menu";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { AppHome } from "./components/AppHome";
import { AppMenu } from "./components/AppMenu";
import { AllFilms } from "./components/films/AllFilms";
import { FilmDetails } from "./components/films/FilmDetails";
import { FilmDelete } from "./components/films/FilmDelete";
import { FilmAdd } from "./components/films/FilmAdd";
import { FilmUpdate } from "./components/films/FilmEdit"
import { FilmActorPayStatistics } from "./components/statistics/FilmActorPayStatistics";


function App() {
	return (
		<React.Fragment>
			<Router>
				<AppMenu />

				<Routes>
					<Route path="/" element={<AppHome />} />
					<Route path="/films" element={<AllFilms />} />
					<Route path="/films/:filmId/details" element={<FilmDetails />} />
					<Route path="/films/:filmId/edit" element={<FilmUpdate />} />
					<Route path="/films/:filmId/delete" element={<FilmDelete />} />
					<Route path="/films/add" element={<FilmAdd />} />
					<Route path="/statistics" element={<FilmActorPayStatistics />} />
				</Routes>
			</Router>
		</React.Fragment>
	);
}

export default App;