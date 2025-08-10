char* addBinary(char* a, char* b) {
    int lenA = strlen(a);
    int lenB = strlen(b);
    int maxLen = (lenA > lenB ? lenA : lenB) + 1; // +1 for possible carry
    char* result = (char*)malloc(maxLen + 1);     // +1 for null terminator

    int i = lenA - 1;
    int j = lenB - 1;
    int k = maxLen; // index for result
    int carry = 0;

    result[k] = '\0'; // null terminate

    while (i >= 0 || j >= 0 || carry) {
        int sum = carry;
        if (i >= 0) sum += a[i--] - '0';
        if (j >= 0) sum += b[j--] - '0';

        result[--k] = (sum % 2) + '0';
        carry = sum / 2;
    }

    // If result starts at index 0
    if (k == 0) {
        return result;
    } else {
        // Shift to remove unused space
        char* finalRes = strdup(result + k);
        free(result);
        return finalRes;
    }
}
