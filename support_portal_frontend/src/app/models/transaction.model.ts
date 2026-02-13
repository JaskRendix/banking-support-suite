export interface Transaction {
  id: number;
  transactionRef: string;
  status: 'PROCESSED' | 'FAILED' | 'PENDING';
  exposureAmount: number;
  errorCode?: string;
}