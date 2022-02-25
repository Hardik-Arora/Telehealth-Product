import React, { useState } from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import Box from '@material-ui/core/Box';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import axios from 'axios';
import GlobalNavbar from '../Navbars/GlobalNavbar/GlobalNavbar';
import constants from '../../constants';
import DoctorModal from './DoctorModal';
import Auxilary from '../../hoc/Auxilary';
import Loader from '../Loader/Loader';
const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(8),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: '100%',
    marginTop: theme.spacing(3),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));
const DoctorRegister = (props) => {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [user, setUser] = useState(null);
  const [modalState, setModalState] = useState(false);
  const [loading,setLoading] = useState(false);
  const handleSubmit = async (event) => {
    event.preventDefault();

    const user = {
      first_name: firstName,
      last_name: lastName,
      email: email,
      password: password,
      is_doctor: true,
      phone_number:phoneNumber
    };
    setLoading(true);
    await axios
      .post(`${constants.API_URL}/register`, user)
      .then((res) => {
        setUser(res.data.user);
        console.log(res);
        console.log(res.data);
        setModalState(true);
        // props.history.push('/login');
      })
      .catch((e) => {
        console.log(e);
      });
    setLoading(false);
  };
  const classes = useStyles();

  const [showModal, setShowModal] = useState(false);

  const openModal = () => {
    console.log("opening modal...")
    setShowModal((prev) => !prev);
  };
  const handleClose = () => {
    setModalState(false);
  };

  return (
    <Auxilary>
      <Loader loading={loading}/>
    <GlobalNavbar />
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div className={classes.paper}>
        <div class="doc-icon" style={{ fontSize: '3rem', color: '#0000ff9e' }}>
          <i class="fas fa-user-md"></i>
        </div>

        <Typography component="h1" variant="h6">
          <b>Welcome Doctor</b>
        </Typography>
        
        <Link href="/register" variant="body2">
          <b>You Can Also Register As a Patient</b>
        </Link>
        <form className={classes.form} noValidate onSubmit={handleSubmit}>
          <Grid container spacing={2}>
            <Grid item xs={12} sm={6}>
              <TextField
                autoComplete="fname"
                name="firstName"
                variant="outlined"
                required
                fullWidth
                id="firstName"
                label="First Name"
                autoFocus
                onChange={(e) => setFirstName(e.target.value)}
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="lastName"
                label="Last Name"
                name="lastName"
                autoComplete="lname"
                onChange={(e) => setLastName(e.target.value)}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="email"
                label="Email Address"
                name="email"
                autoComplete="email"
                onChange={(e) => setEmail(e.target.value)}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                name="password"
                label="Password"
                type="password"
                id="password"
                autoComplete="current-password"
                onChange={(e) => setPassword(e.target.value)}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="PhoneNumber"
                label="Phone Number"
                name="Phone Number"
                autoComplete="number"
                onChange={(e) => setPhoneNumber(e.target.value)}
              />
            </Grid>
            {/* <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="specialization"
                label="specialization"
                name="specialization"
                autoComplete="text"
                // onChange={e => setPhoneNumber(e.target.value)}
              />
            </Grid> */}
            <Grid item xs={12}>
              <FormControlLabel
                control={<Checkbox value="allowExtraEmails" color="primary" />}
                label="I want to receive inspiration, marketing promotions and updates via email."
              />
            </Grid>
          </Grid>
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            className={classes.submit}
          >
            Register
          </Button>
          <Grid container justify="flex-end">
            <Grid item>
              <Link href="/login" variant="body2">
                Already have an account? Log in
              </Link>
              <br />
            </Grid>
          </Grid>
        </form>
      </div>
      <Box mt={5}></Box>
    </Container>
    {modalState ? <DoctorModal isOpen={true} onClose={handleClose} email={email} password={password} /> : null}
    </Auxilary>);
};

export default DoctorRegister;
