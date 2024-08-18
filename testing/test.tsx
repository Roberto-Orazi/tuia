import '@testing-library/jest-dom'
import { fireEvent, render } from '@testing-library/react'
import { Raffle } from '../../../types/types'
import { RaffleCollapse } from './RaffleCollapse'

const mockRaffle: Raffle = {
  id: 1,
  price: 100,
  title: 'Raffle 1',
  caption: 'Caption 1',
  description1: 'Description 1',
  description2: 'Description 2',
  prizeType: 'Car',
  media: {
    images: [
      {
        url: 'image-url',
        thumbnailUrl: 'thumbnail-url',
        fileResourceId: 123
      }
    ]
  },
  ticketsSold: 10,
  endsAt: new Date(),
  winnerAddress: '0x1234567890abcdef',
  ticketsOwned: 1,
  ended: false
}

describe('RaffleCollapse', () => {
  it('should render raffle title and description1', () => {
    const { getByText } = render(<RaffleCollapse raffle={mockRaffle} />)
    expect(getByText('Raffle 1 Description 1')).toBeInTheDocument()
  })

  it('should render price, tickets sold and winner', () => {
    const { getByText } = render(<RaffleCollapse raffle={mockRaffle} />)
    expect(getByText('Price:')).toBeInTheDocument()
    expect(getByText('Tickets sold:')).toBeInTheDocument()
    expect(getByText('Winner:')).toBeInTheDocument()
  })

  it('should copy winner address to clipboard when copy button is clicked', () => {
    const { getByTitle } = render(<RaffleCollapse raffle={mockRaffle} />)
    const copyButton = getByTitle('Copy address')

    Object.assign(navigator, {
      clipboard: {
        writeText: jest.fn().mockImplementation(() => Promise.resolve())
      }
    })

    fireEvent.click(copyButton)
    expect(navigator.clipboard.writeText).toHaveBeenCalledWith('0x1234567890abcdef')
  })

  it('should display "No winner" when winnerAddress is undefined', () => {
    const raffleWithoutWinner = { ...mockRaffle, winnerAddress: undefined }
    const { getByText } = render(<RaffleCollapse raffle={raffleWithoutWinner} />)
    expect(getByText('No winner')).toBeInTheDocument()
  })
})

collapse


import { FileCopy } from '@mui/icons-material'
import { Box, Card, Chip, IconButton, Typography } from '@mui/material'
import Grid from '@mui/material/Unstable_Grid2'
import { Raffle } from '../../../types/types'
import { displayWallet } from '../../../utils/wallet.helper'

interface Props {
  raffle: Raffle
}
export const RaffleCollapse = ({ raffle }: Props) => {
  return (
    <Card
      sx={{
        position: 'relative',
        border: '1px solid black',
        margin: '1rem 0',
        padding: '1rem',
        cursor: { xs: 'pointer', md: 'default' },
        transition: 'background-color 0.3s'
      }}
    >
      <Grid
        container
        xs={12}
        padding={1}
        display={{
          xs: 'flex',
          cursor: 'pointer'
        }}
      >
        <Grid xs={12} sm={6} lg={10}>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
            <Typography
              style={{ fontSize: window.innerWidth <= 600 ? '0.8rem' : '1rem' }}
              fontWeight="bold"
            >
              {raffle.title} {raffle.description1}
            </Typography>
          </Box>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
            <Typography
              style={{ fontSize: window.innerWidth <= 600 ? '0.8rem' : '1rem' }}
            >
              <span style={{ fontWeight: 'bold' }}>Description 2:</span>{' '}
            </Typography>
            <Chip label={raffle.description2} />
          </Box>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
            <Typography
              style={{ fontSize: window.innerWidth <= 600 ? '0.8rem' : '1rem' }}
            >
              <span style={{ fontWeight: 'bold' }}>Price:</span>{' '}
            </Typography>
            <Chip label={raffle.price} />
          </Box>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
            <Typography
              style={{ fontSize: window.innerWidth <= 600 ? '0.8rem' : '1rem' }}
            >
              <span style={{ fontWeight: 'bold' }}>Tickets sold:</span>{' '}
            </Typography>
            <Chip label={raffle.ticketsSold} />
          </Box>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
            <Typography
              style={{ fontSize: window.innerWidth <= 600 ? '0.8rem' : '1rem' }}
            >
              <span style={{ fontWeight: 'bold' }}>Winner:</span>{' '}
            </Typography>
            {raffle?.winnerAddress ? (
              <>
                <Chip label={displayWallet(raffle.winnerAddress)} />
                <IconButton
                  title="Copy address"
                  onClick={() => navigator.clipboard.writeText(raffle.winnerAddress)}
                  size="small"
                  style={{ marginLeft: 8, color: 'black' }}
                >
                  <FileCopy fontSize="small" sx={{ color: 'black' }} />
                </IconButton>
              </>
            ) : (
              <Chip label="No winner" />
            )}
          </Box>
        </Grid>
      </Grid>
    </Card>
  )
}



form

import '@testing-library/jest-dom'
import { fireEvent, render, screen, waitFor } from '@testing-library/react'
import { CreateRaffleDto } from '../../../validations/raffle.dto'
import { RaffleForm } from './RaffleForm'

jest.mock('../../../services/raffles.service', () => ({
  createRaffle: jest.fn(),
  updateRaffle: jest.fn()
}))

jest.mock('notistack', () => ({
  useSnackbar: () => ({
    enqueueSnackbar: jest.fn()
  })
}))

const mockRaffle: CreateRaffleDto = {
  title: 'Test Title',
  description1: 'Test Description 1',
  description2: 'Test Description 2',
  image: { url: 'test-url' },
  endsAt: '06/18/2024, 12:45 PM',
  price: 100
}

describe('RaffleForm', () => {
  it('should render the RaffleForm component', () => {
    render(
      <RaffleForm
        refetchRaffles={() => {}}
        title="Add"
        initialValues={mockRaffle}
        onReset={() => {}}
      />
    )

    expect(screen.getByText('Add Raffle')).toBeInTheDocument()
  })

  it('should render input fields with initial values', () => {
    render(
      <RaffleForm
        refetchRaffles={() => {}}
        title="Update"
        initialValues={mockRaffle}
        onReset={() => {}}
      />
    )

    expect(screen.getByLabelText('Title')).toHaveValue('Test Title')
    expect(screen.getByLabelText('Description 1')).toHaveValue('Test Description 1')
    expect(screen.getByLabelText('Description 2')).toHaveValue('Test Description 2')
    expect(screen.getByLabelText('Ends at')).toHaveValue(mockRaffle.endsAt)
    expect(screen.getByLabelText('Price')).toHaveValue(100)
  })

  it('should call createRaffle mutation on form submission when in create mode', async () => {
    const { createRaffle } = require('../../../services/raffles.service')
    createRaffle.mockResolvedValue({})

    render(
      <RaffleForm
        refetchRaffles={() => {}}
        title="Add"
        initialValues={mockRaffle}
        onReset={() => {}}
      />
    )

    fireEvent.click(screen.getByRole('button', { name: /save/i }))

    await waitFor(() => {
      expect(createRaffle).toHaveBeenCalledWith(mockRaffle)
    })
  })

  it('should call updateRaffle mutation on form submission when on Update mode', async () => {
    const { updateRaffle } = require('../../../services/raffles.service')
    updateRaffle.mockResolvedValue({})

    render(
      <RaffleForm
        refetchRaffles={() => {}}
        title="Update"
        initialValues={mockRaffle}
        onReset={() => {}}
      />
    )

    fireEvent.click(screen.getByRole('button', { name: /save/i }))

    await waitFor(() => {
      expect(updateRaffle).toHaveBeenCalledWith(mockRaffle)
    })
  })

  it('should reset form values and call onReset when reset button is clicked', () => {
    const onReset = jest.fn()

    render(
      <RaffleForm
        refetchRaffles={() => {}}
        title="Update"
        initialValues={mockRaffle}
        onReset={onReset}
      />
    )

    fireEvent.click(screen.getByRole('button', { name: /reset/i }))

    expect(screen.getByLabelText('Title')).toHaveValue('')
    expect(screen.getByLabelText('Description 1')).toHaveValue('')
    expect(screen.getByLabelText('Description 2')).toHaveValue('')
    expect(screen.getByLabelText('Ends at')).toHaveValue('06/18/2024, 12:45 PM')
    expect(screen.getByLabelText('Price')).toHaveValue(0)

    expect(onReset).toHaveBeenCalled()
  })
})
