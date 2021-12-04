import React from 'react';
import { Link } from 'react-router-dom';
import { Container, Flex, Heading, Spacer, Box, Button } from '@chakra-ui/react';
import { FaUser } from 'react-icons/fa';

function Header() {
  const isAuthenticated = true;

  return (
    <Container maxW="container.xl">
      <Flex>
        <Link to="/">
          <Heading>Nice Chat</Heading>
        </Link>
        <Spacer />
        {isAuthenticated ? (
          <Box p="2">
            <Link to="/user/me">
              <Button leftIcon={<FaUser />}>Account</Button>
            </Link>
          </Box>
        ) : (
          <>
            <Box p="2">
              <Link to="/auth/login">
                <Button>Login</Button>
              </Link>
            </Box>
            <Box p="2">
              <Link to="/auth/register">
                <Button>Register</Button>
              </Link>
            </Box>
          </>
        )}
      </Flex>
    </Container>
  );
}

export default Header;
