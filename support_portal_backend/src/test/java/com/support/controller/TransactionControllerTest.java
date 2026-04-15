package com.support.controller;

import com.support.model.Transaction;
import com.support.repository.TransactionRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import java.util.Arrays;
import java.util.Collections;

import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@WebMvcTest(TransactionController.class)
public class TransactionControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private TransactionRepository repository;

    @Test
    public void shouldReturnAllTransactions() throws Exception {
        // Arrange: Create a mock transaction
        Transaction t1 = new Transaction();
        t1.setId(1L);
        t1.setTransactionRef("REF-123");
        t1.setStatus("FAILED");
        t1.setExposureAmount(500.0);

        when(repository.findAll()).thenReturn(Arrays.asList(t1));

        // Act & Assert: Perform the GET request and check the JSON
        mockMvc.perform(get("/api/support/transactions"))
                .andExpect(status().isOk())
                .andExpect(content().contentType(MediaType.APPLICATION_JSON))
                .andExpect(jsonPath("$[0].transactionRef").value("REF-123"))
                .andExpect(jsonPath("$[0].status").value("FAILED"))
                .andExpect(jsonPath("$[0].exposureAmount").value(500.0));
    }

    @Test
    public void shouldReturnTransactionsByStatus() throws Exception {
        // Arrange
        Transaction t1 = new Transaction();
        t1.setStatus("PROCESSED");
       
        when(repository.findByStatus("PROCESSED")).thenReturn(Arrays.asList(t1));

        // Act & Assert
        mockMvc.perform(get("/api/support/transactions/status/PROCESSED"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$[0].status").value("PROCESSED"));
    }

    @Test
    public void shouldReturnEmptyListWhenNoTransactionsFound() throws Exception {
        // Arrange
        when(repository.findByStatus("PENDING")).thenReturn(Collections.emptyList());

        // Act & Assert
        mockMvc.perform(get("/api/support/transactions/status/PENDING"))
                .andExpect(status().isOk())
                .andExpect(content().json("[]"));
    }
}