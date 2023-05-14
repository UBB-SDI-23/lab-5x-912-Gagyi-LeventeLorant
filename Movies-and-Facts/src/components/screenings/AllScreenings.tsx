import {
	TableContainer,
	Paper,
	Table,
	TableHead,
	TableRow,
	TableCell,
	TableBody,
	CircularProgress,
	Container,
	IconButton,
	Tooltip,
	Toolbar,
	Button,
} from "@mui/material";
import React from "react";
import { useEffect, useState } from "react";
import { Await, Link } from "react-router-dom";
import { BACKEND_API_URL } from "../../constants";
import { Film } from "../../models/Film";
import ReadMoreIcon from "@mui/icons-material/ReadMore";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import AddIcon from "@mui/icons-material/Add";
import ArrowForwardIosIcon from '@mui/icons-material/ArrowForwardIos';
import ArrowBackIosIcon from '@mui/icons-material/ArrowBackIos';
import { Screening } from "../../models/Screening";

export const AllScreenings = () => {
	const [loading, setLoading] = useState(false);
	const [screenings, setScreenings] = useState<Screening[]>([]);
    const [currentPage, setCurrentPage] = useState(1);
    const totalPages = Math.ceil(1000000 / 10);

	

	useEffect(() => {
		setLoading(true);
		fetch(`${BACKEND_API_URL}/screenings/?page=${currentPage}`)
			.then((response) => response.json())
			.then((data) => {
				setScreenings(data);
				setLoading(false);
			});
	}, []);


	const handleNextPage = () => {
		if (currentPage < totalPages) {
		  
		  setCurrentPage(currentPage + 1);
		  console.log(currentPage);
		  setLoading(true);
		  fetch(`${BACKEND_API_URL}/screenings/?page=${currentPage}`)
		  .then((response) => response.json())
		  .then((data) => {
			setScreenings(data);
			setLoading(false);
		  });
		  
		}
	  };

	  const handlePrevPage = () => {
		if (currentPage > 1) {
		  
		  setCurrentPage(currentPage - 1);
		  console.log(currentPage);
		  setLoading(true);
		  fetch(`${BACKEND_API_URL}/screenings/?page=${currentPage}`)
		  .then((response) => response.json())
		  .then((data) => {
			setScreenings(data);
			setLoading(false);
		  });
		   
		}
	  };


	async function getFilmName(film: number): Promise<React.ReactNode> {
		const response = await fetch(`${BACKEND_API_URL}/films/${film}`);
		const filmname = await response.json();
		return Promise.resolve(filmname.name);
	}

	return (
		<Container>
			<h1>All screenings</h1>

			{loading && <CircularProgress />}
			{!loading && screenings.length === 0 && <p>No screenings found</p>}
			{!loading && (
				<Toolbar>
					<IconButton onClick={handlePrevPage} style={{ marginRight:'370px'}} component={Link} sx={{ mr: 3 }} to={`/screenings/?p=${currentPage}`} disabled={currentPage === 1}>
					<Tooltip title="Previous">
					<ArrowBackIosIcon sx={{ color: "white" }} />
					</Tooltip>
				</IconButton>
				<IconButton component={Link} sx={{ mr: 3 }} to={`/screenings/add`}>
					<Tooltip title="Add a new screening" arrow>
						<AddIcon color="primary" />
					</Tooltip>
				</IconButton>
					<IconButton style={{ marginLeft:'370px'}} onClick={handleNextPage} component={Link} sx={{ mr: 3 }}  to={`/screenings/?p=${currentPage}`} disabled={currentPage === totalPages}>
            		<Tooltip title="Next">
             		<ArrowForwardIosIcon sx={{ color: "white" }} />
            		</Tooltip>
          			</IconButton>
					</Toolbar>
			)}
			{!loading && screenings.length > 0 && (
				<TableContainer component={Paper}>
					<Table sx={{ minWidth: 650 }} aria-label="simple table">
						<TableHead>
							<TableRow>
								<TableCell>#</TableCell>
								<TableCell align="right">Room</TableCell>
								<TableCell align="right">Date</TableCell>
								<TableCell align="right">Price</TableCell>
								<TableCell align="right">Film</TableCell>
								<TableCell align="center">Operations</TableCell>
							</TableRow>
						</TableHead>
						<TableBody>
							{screenings.map((screening, index) => (
								<TableRow key={screening.id}>
									<TableCell component="th" scope="row">
										{index + 1}
									</TableCell>
									<TableCell component="th" scope="row">
										<Link to={`/screenings/${screening.id}/details`} title="View screening details">
											{screening.room}
										</Link>
									</TableCell>
									<TableCell align="right">{screening.date}</TableCell>
									<TableCell align="right">{screening.price}</TableCell>
									<TableCell component="th" scope="row">
										<Link to={`/films/${screening.film}/details`} title="View film details">
											{screening.film}
										</Link>
									</TableCell>
									<TableCell align="right">
										<IconButton
											component={Link}
											sx={{ mr: 3 }}
											to={`/screenings/${screening.id}/details`}>
											<Tooltip title="View screening details" arrow>
												<ReadMoreIcon color="primary" />
											</Tooltip>
										</IconButton>

										<IconButton component={Link} sx={{ mr: 3 }} to={`/screenings/${screening.id}/edit`}>
											<EditIcon />
										</IconButton>

										<IconButton component={Link} sx={{ mr: 3 }} to={`/screenings/${screening.id}/delete`}>
											<DeleteForeverIcon sx={{ color: "red" }} />
										</IconButton>
									</TableCell>
								</TableRow>
							))}
						</TableBody>
					</Table>
				</TableContainer>
			)}
		</Container>
	);
};